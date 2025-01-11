#!/bin/env ruby
require 'json'
require 'shellwords'

# Parse images with tesseract

`ls *.png`.split("\n").each_with_index { |f, i| `tesseract #{Shellwords.escape(f)} #{i} --psm 6 && cat #{i}.txt >> /tmp/output.txt` }

require 'awesome_print'
@capts = {}
File.read('/tmp/output.txt').split("\n").each {|l| name, points = l.match(/\(ELA\)(.*)\s(\d+)$/)&.captures; @capts[name.strip] ||= points.to_i if name && points };nil

`rm /tmp/output.txt`

File.open(Time.now.strftime('donaciones-%y-%m-%d.json'), 'w') {|f| f.write @capts.sort_by { |k, p| p.to_i }.reverse.to_h.to_json }
