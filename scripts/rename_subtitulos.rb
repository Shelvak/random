require 'shellwords'

ext = ARGV.first || 'mkv'
subs = `ls *.srt`.split("\n")
caps = `ls *.#{ext}`.split("\n")

with_sub = {}

subs.each do |sub|
  s, e = sub.match(/(\d+)x(\d+).*.srt$/)&.captures
  s, e = sub.match(/S(\d+)E(\d+).*.srt$/)&.captures unless s
  puts s, e

  matchs = [/S#{s}E#{e}/, /#{s}x#{e}/]

  cap = caps.find { |c| c.match?(matchs.first) || c.match?(matchs.last) }

  sub_index = with_sub[cap] ? '' : ".#{with_sub[cap]}"
  sub_name = cap.gsub('.mkv', sub_index)

  with_sub[cap] ||= 0
  with_sub[cap]  += 1

  `mv #{Shellwords.escape(sub)} #{sub_name}.srt`
end
