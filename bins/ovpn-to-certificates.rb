#!/usr/bin/env ruby

def extract(part, contents, file)
  pattern = /\<#{part}\>(.*)\<\/#{part}\>/m
  m = contents.match pattern

  return contents if m.nil?

  File.open(file, "w") {|f| f.write m[1].strip }
end

path = ARGV[0]
original_ovpn = File.read(path)
filename = path.split('/').last
cert_name = File.basename(filename, File.extname(filename))

extract('ca',       original_ovpn, "#{cert_name}-ca.crt")
extract('key',      original_ovpn, "#{cert_name}-client.key")
extract('cert',     original_ovpn, "#{cert_name}-client.crt")
extract('tls-auth', original_ovpn, "#{cert_name}-ta.key")
