#!/home/rotsen/.rubies/ruby-2.6.8/bin/ruby

# Ignore params to skip "tracking"
DROP_PARAMS_DOMAINS = [
  /^https:\/\/twitter.com\//
]

# 100% trusted domains
TRUSTED_DOMAINS = [
  /^https:\/\/github.com\//
]

DEFAULT_BROWSER = 'firefox'
DEFAULT_PRIVATE_BROWSER = 'firefox -private-window'

# Log to journal
def log(string)
  `echo '#{string}' | systemd-cat -t custom-open-link`
end

def drop_params(url)
  clean = url.match(/^(http.*)\?.*/)&.captures&.first
  open(clean) if clean
end

def open(url)
  `#{DEFAULT_BROWSER} #{url}`
end

def private_open(url)
  `#{DEFAULT_PRIVATE_BROWSER} #{url}`
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
