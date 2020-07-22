
capitulos = {}

`ls  ~/raspi/Stargate.Atlantis.S02.1080p.BluRay.x264-P0W4HD[rartv]`.split("\n").each do |line|
  cap = line.to_s.match(/(S\d+E\d+)/i)&.captures&.first

  capitulos[cap] = line.strip.gsub(/\.mkv$/, '')
end

subs = `cd ~/raspi/papa/; ls *.srt`.split("\n")

capitulos.each do |cap, file|
  subs.select { |subtitle| subtitle.match?(/#{cap}/i) }.each_with_index do |sub, i|
    `cd ~/raspi/papa; cp #{Shellwords.escape(sub)} a/#{Shellwords.escape(file)}#{".#{i}" if i.positive?}.srt`
  end
end

`cd ~/raspi/papa; ls `.split()
