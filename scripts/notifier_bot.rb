require 'cgi'
# require 'rest-client'


def send_text(text)
  bot_id = "botNNNN:botCode"
  chat_id = "chat_id"
  url = "https://api.telegram.org/#{bot_id}/sendMessage?chat_id=#{chat_id}&text="

  puts url
  puts text
  puts CGI.escape(text)
  puts url + CGI.escape(text)
  #RestClient::Request.execute(
  puts `curl -X GET "#{url + CGI.escape(text)}"`
  sleep 1
end
