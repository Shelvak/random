#!/home/rotsen/.rubies/ruby-2.6.8/bin/ruby
require 'uri'
require 'net/http'
require 'json'
require 'time'

DOMAIN = "https://px1.tuyaus.com"
SESSION_URL = "#{DOMAIN}/homeassistant/auth.do"

def new_session
  data = {user: "USER", pass: "PASS"}

  uri = URI(SESSION_URL)
  res = Net::HTTP.post_form(
    uri,
    userName: data[:user],
    password: data[:pass],
    countryCode: '11',
    bizType: 'smart_life',
    from: 'tuya'
  )
  body = JSON.parse(res.body) if res.is_a?(Net::HTTPSuccess)
end

def session
  @_session ||= begin
                  credentials = JSON.parse(File.read('/tmp/smartlife.cred')) rescue {}
                  expire_at   = Time.parse(credentials['expires_at']) rescue nil

                  if (expire_at.nil? || expire_at < Time.now)
                    credentials = new_session
                    credentials['expires_at'] = (Time.new + credentials['expires_in'])
                  end

                  File.open('/tmp/smartlife.cred', 'w') { |f| f.write credentials.to_json }

                  credentials['access_token']
                end
end

def change_switch(on)
  headers = { 'Content-Type': 'application/json' }
  header = {
    'name': 'turnOnOff',
    'namespace': 'control',
    'payloadVersion': 1,
  }
  payload = {
    value: (on ? '1' : '0'),
    accessToken: session,
    devId: "DEV_ID"
  }

  data = {
    header: header,
    payload: payload
  }
  uri = URI("#{DOMAIN}/homeassistant/skill")
  res = Net::HTTP.post(uri, data.to_json, headers)
  # pp res.body
  # body = JSON.parse(res.body) if res.is_a?(Net::HTTPSuccess)
end

if ARGV.size > 0 && ARGV[0] == 'Off'
  # puts "Apagando"
  change_switch(false) # turn off
else
  # puts "prendiendo"
  change_switch(true) # turn on
end
