require 'shellwords'

### texlive-core [required]

files = ARGV.any? ? ARGV : `ls *.pdf`.split("\n")

puts "Cropping... #{files.size} files"
files.each_with_index do |file, i|
  `pdfcrop --margins '-5 -5 -5 -5' #{Shellwords.escape(file)} cropped_#{i}.pdf`
end

puts 'Joining...'
(0..(files.size - 1)).each_slice(9).each_with_index do |group, gi|
  file_names = group.map {|i| "cropped_#{i}.pdf" }.join(' ')
  `pdfnup --nup 3x3 --no-landscape #{file_names} --outfile grouped_#{gi}.pdf`
end
puts 'Done =D'
