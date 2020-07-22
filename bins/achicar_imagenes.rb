files = `find _assets/ -iname "*.png" -type f -exec identify -format '%w %h %i' '{}' \\; | awk '$1>1000 || $2>1000'`
filtered_files = files.split('.png').map {|e| w, h, file = *e.split(' '); file if w.to_i > 1000 || h.to_i > 1000 }.flatten.compact.uniq.map {|e| e + '.png'}

filtered_files.each {|file| `convert #{file} -resize 1000x1000\\> #{file}` }
