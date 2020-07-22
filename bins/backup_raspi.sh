#/!/bin/zsh

# cd /run/media/rotsen/Hulk/Backup-RotseN/

scp -r raspi:notifier_bot.rb ./raspi/
scp -r raspi:transmission.rb ./raspi/
scp -r raspi:.config/transmission-daemon ./raspi/
scp -r raspi:/media/Torrents/.flexget/config.yml ./raspi/flexget/
scp -r raspi:/media/Torrents/.flexget/db-config.sqlite ./raspi/flexget/


cp -Rv ~/bins .

