require 'date'
require 'nokogiri'

require '/home/rotsen/notifier_bot'

output = `curl 'https://www.mrturno.com/turn/create?from=microsite&professional_id=ef5c0422-44dd-11eb-9134-0ae01a288093&institution_subsidiary_id=34571667-9c8a-11ea-a720-de31932e4d21' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: es-AR,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Connection: keep-alive' -H 'Cookie: advanced-frontend-mobile-web=0b7c20377968359023d12dc8caa2c09a; mt5_microsite_slug=263da533bcb01083eb49a8f4a180d418a04d0f6500d5861dc6e541ae370228c2a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22mt5_microsite_slug%22%3Bi%3A1%3Bs%3A3%3A%22cmp%22%3B%7D; _csrf-frontend=fe13c8eaa1bb44683bd9871c46d75d1da2a2076f03078dca58b6a38746975a5da%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22UHFQKJ5b-umMc1_wZQubV2QA1f5n5QZz%22%3B%7D' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: none' -H 'Sec-Fetch-User: ?1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache'`

puts output

availables = []
Nokogiri::HTML(output).search('[name="NewTurnForm[free_turn_slot_id]"] option').each do |opt|
  raw_date, h, m = opt.text.match(/\w+ (\d+\/\d+) - (\d+):(\d+) hs/i)&.captures

  if raw_date
    date = Date.parse("#{raw_date}/2021")
    if date < Date.new(2022,2,1) && h.to_i >= 10
      availables << "#{date} #{h}:#{m}hs "
    end
  end
end

if availables.any?
  send_text [
    'TURNO DISPONIBLE: ',
    availables[0..5],
    'https://www.mrturno.com/turn/create?from=microsite&professional_id=ef5c0422-44dd-11eb-9134-0ae01a288093&institution_subsidiary_id=34571667-9c8a-11ea-a720-de31932e4d21'
  ].flatten.join("\n")
end
