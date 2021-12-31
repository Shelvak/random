#!/home/rotsen/.rubies/ruby-2.6.8/bin/ruby

# Ignore params to skip "tracking"
DROP_PARAMS_DOMAINS = [
  /^https:\/\/twitter.com\//
]

# 100% trusted domains
TRUSTED_DOMAINS = [
  /^https:\/\/github.com\//
]

# Log to journal
def log(string)
  `echo '#{string}' | systemd-cat -t custom-open-link`
end

def drop_params(url)
  clean = url.match(/^(http.*)\?.*/)&.captures&.first
  open(clean)
end

def open(url)
  `firefox #{url}`
end

def private_open(url)
  `firefox -private-window #{url}`
end

def filter_url(url)
  case url
  when *DROP_PARAMS_DOMAINS then drop_params(url)
  when *TRUSTED_DOMAINS then open(url)
  else
    log("Unknown: #{url}")

    private_open(url)
  end
end


filter_url ARGV[0]
