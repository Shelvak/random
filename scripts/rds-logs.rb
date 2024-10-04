rds = 'production-eks-pg-cloud'

files = `/root/.local/bin/aws rds describe-db-log-files --db-instance-identifier #{rds} | jq -r '.DescribeDBLogFiles[] | .LogFileName'`.split("\n")

threads = files.map do |raw_file|
  file = raw_file.gsub('error/', '')

  # next if File.exists?("/usr/src/logs/rds/#{file}")

  # Thread.new do
    puts "Downloading #{file}"

    last    = 0
    prev    = 0
    counter = 0

    loop do
      prev       = last
      debug_file = "#{file}.#{counter}.debug"

      `/root/.local/bin/aws rds download-db-log-file-portion --db-instance-identifier #{rds} --log-file-name "#{raw_file}" --starting-token #{last}  --debug --output text 2>>#{debug_file} >> #{file}.#{counter}`

      debug = File.read(debug_file)
      # last = debug # hacer algo
      last = debug.scan(/<Marker>(\d:\d+)<\/Marker>/).flatten.last

      # grep "<Marker>"  | tail -1 | tr -d "<Marker>" | tr -d "/" | tr -d " "`

      if prev.to_s == last.to_s
        # `rm #{file}.#{counter}`
        # `rm #{debug_file}`
        break
      else
        prev = last
      end

      `cat #{file}.#{counter} >> /usr/src/logs/rds/#{file}`

      `rm #{file}.#{counter}`
      `rm #{debug_file}`

      counter += 1
    end
    puts "#{file} done"
rescue ::Exception => e
  puts e
end # .compact.each(&:join)
