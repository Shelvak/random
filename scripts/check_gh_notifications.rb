require 'json'

notifications = JSON.parse(
  `curl "https://api.github.com/notifications?access_token=#{"token_access"}"`
).map { |n| n['id'] }.uniq

old_notifications = File.open('/tmp/gh_notifications', 'r').read.split("\n")

if (notifications - old_notifications).any?
  `notify-send --hint=int:transient:1 -u low "New notifications" "https://github.com/notifications"`
end

File.open('/tmp/gh_notifications', 'a') { |f| f.write(notifications) }
