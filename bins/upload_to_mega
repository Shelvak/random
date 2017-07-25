#!/usr/bin/env ruby

require 'rmega'

storage = Rmega.login('ACC', 'PASS')

backup = storage.nodes.find {|node| node.type == :folder && node.name == 'DIR_NAME' }

ARGV.each do |file|
  puts file
  backup.upload(file)
end

