ARGV.each do |path|
  file = File.open(path).read

  file.gsub!(/<\/ i>/i, '</i>')
  file.gsub!(/<i>/i, '<i>')
  file.gsub!(': ', ':')
  file.gsub!('->', '-->')

  File.open("#{path}-new", 'w') {|f| f.write(file)}
end
