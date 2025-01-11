subs = `ls *.srt`.split("\n")
caps = `ls ../Stargate.Atlantis.S01.1080p.BluRay.x264-P0W4HD\\[rartv\\]/*.mkv`.split("\n")
caps.each do |cap|
  n = cap.match(/(S01E\d{2})/)[1]
  n_sub = subs.grep(/#{n}/i)
  name = cap.split('/').last.delete('.mkv')
  n_sub.each_with_index do |s, i|
    `mv #{s} #{name}#{i}.srt`
  end
end
