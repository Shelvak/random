require 'active_support/core_ext/array'

file_numbers = Dir['/home/rotsen/Imágenes/backgrounds/*'].map { |e| d = e.match(/\d+/); d ? d[0].to_i : nil }.compact.uniq.sort;nil
numbers = ((1..70000).to_a - file_numbers).sort.in_groups_of(50);nil

numbers.each do |group|
  group.each do |i|
    `wget -bq http://alpha.wallhaven.cc/wallpapers/full/wallhaven-#{i}.jpg`
  end

  loop do
    sleep 10
    break if `ps aux |grep wget |wc -l`.to_i < 20
  end

  puts group.last
end
