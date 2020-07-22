require 'httpclient'

body = JSON.parse(HTTPClient.get('http://29574e.ethosdistro.com/?json=yes').body)
"sudo reboot" if body['total_hashes'] < 3000


