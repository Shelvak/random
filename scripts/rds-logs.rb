#!/usr/bin/env ruby

# Download RDS logs and compress them


require 'json'

rds      = 'production-eks'
main_dir = '/usr/src/logs/rds/'
aws      = '/root/.local/bin/aws'
bucket   = 'rds-logs'

def exec(cmd)
  # Just in case we want to change the `shell exec`
  `#{cmd}`
end

files = JSON.parse(
  exec([
    aws,
    'rds describe-db-log-files',
    "--db-instance-identifier #{rds}"
  ].join(' '))
)['DescribeDBLogFiles'][0..-2] # skip "still working" last file

# files = ['error/postgresql.log.2020-09-01-12']

files.each do |raw_file|
  file      = raw_file.gsub('error/', '')
  full_file = main_dir + file

  if File.exists?(full_file) || File.exists?(full_file.gsub(/-\d{2}$/, '') + '.tar.zst')
    puts "Skipping #{file}"
    next
  end

  puts "Downloading #{file}"

  current_pointer = 0
  last_pointer    = 0
  counter         = 0

  loop do
    last_pointer = current_pointer
    counter_file = "#{file}.#{counter}"
    debug_file   = "#{counter_file}.debug"

    exec([
      aws,
      "rds download-db-log-file-portion",
      "--db-instance-identifier #{rds}"
      "--log-file-name #{raw_file}",
      "--starting-token #{current_pointer}",
      "--debug --output text"
      "2>>#{debug_file} >> #{counter_file}"
    ].join(' '))

    current_pointer = File.read(debug_file).scan(/Marker>(\d+:\d+)<\/Marker/).flatten.last

    if last_pointer.to_s == current_pointer.to_s
      exec("rm #{counter_file} #{debug_file}")

      break
    else
      last_pointer = current_pointer
    end

    exec("cat #{counter_file} >> #{full_file}")
    exec("rm #{counter_file} #{debug_file}")

    counter += 1
  end
  puts "#{file} done"
rescue ::Exception => e
  puts "ERROR: #{e.message}"
  puts e.backtrace
end

files = exec("cd #{main_dir}; ls postgresql.log.*")
dates = files.scan(/postgresql.log.(\d{4}\-\d{2}\-\d{2})/).flatten.uniq
range = ('00'..'23').to_a

dates.each do |date|
  full_file = main_dir + 'postgresql.log.' + date
  zst       = full_file + '.tar.zst'

  next if File.exists?(zst)

  # Ensure completed date
  if range.all? { |postfix| files.match? /#{date}-#{postfix}$/ }
    # Compress full date
    exec("cd #{main_dir}; tar -cvf - #{full_file}-* | zstd -T3 > #{zst}")

    # Upload compressed full date
    exec("#{aws} s3 cp #{zst} s3://#{bucket}/")
  end
end
