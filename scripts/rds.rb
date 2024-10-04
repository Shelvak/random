rds      = 'production-eks-pg-cloud'
main_dir = '/tmp/logs'

files = `aws rds describe-db-log-files --db-instance-identifier #{rds} | jq -r '.DescribeDBLogFiles[] | .LogFileName'`.split("\n")

files.each do |raw_file|
  file      = raw_file.sub('error/', '')
  full_file = "#{main_dir}/#{file}"

  next if File.exists?(full_file)

  puts "Downloading #{file}"

  current = 0
  last    = nil
  counter = 0

  until current.to_s == last.to_s do
    debug_file   = "#{file}.#{counter}.debug"
    counter_file = "#{file}.#{counter}"

    `aws rds download-db-log-file-portion --db-instance-identifier #{rds} --log-file-name "#{raw_file}" --starting-token #{current}  --debug --output text 2>>#{debug_file} >> #{counter_file}`

    last    = current
    current = File.read(debug_file).scan(/<Marker>(\d:\d+)<\/Marker>/).flatten.last

    `cat #{counter_file} >> #{full_file}`

    counter += 1
  end

  puts ".... done"
rescue ::Exception => e
  puts e
end
