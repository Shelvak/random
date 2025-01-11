#!/bin/ruby

require 'json'
require 'shellwords'
require File.expand_path(File.dirname(__FILE__)) + '/notifier_bot'

torrent_name = Shellwords.escape(ENV['TR_TORRENT_NAME'])

guess_result = JSON.parse(`/media/Torrents/.flexget/flexget-bin/bin/guessit -j #{torrent_name}`.strip)

title = if guess_result['type'] == 'movie'
          guess_result.values_at('title', 'year').join ' - '
        else
          [
            guess_result['title'],
            [guess_result['season'], guess_result['episode'].to_s.rjust(2, '0')].join('x'),
            "\n",
            guess_result['episode_title']
          ].compact.join ' '
        end

`touch /media/Torrents/#{torrent_name}/.check_for_dts`
`/home/rotsen/bins/refresh_plex`
send_text "Torrent Completo: \n#{title}"
