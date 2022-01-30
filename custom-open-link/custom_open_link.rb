#!/home/rotsen/.rubies/ruby-2.6.8/bin/ruby

# Ignore params to skip "tracking"
DROP_PARAMS_DOMAINS = [
  /^https:\/\/twitter\.com\//
]

# 100% trusted domains
TRUSTED_DOMAINS = [
  /^https:\/\/github\.com\//,
  /^https:\/\/.*cloud\.wispro\.co\//,
  /^https:\/\/docs\.google\.com\//
]

# Links to open with alternative browser
ALT_BROWSER_DOMAINS = [
  /^https:\/\/app\.\//,
  /^https:\/\/\S+\.finance/
]

DEFAULT_BROWSER = 'firefox'
DEFAULT_PRIVATE_BROWSER = 'firefox -private-window'
ALT_BROWSER = 'google-chrome-stable'

# Log to journal
def log(string)
  `echo '#{string}' >> /tmp/custom-open-link`
  `echo '#{string}' | systemd-cat -t custom-open-link`
end

def drop_params(url)
  clean = url.split('?').first
  open(clean) if clean
end

def open(url)
  log("Opening: #{url}")
  `#{DEFAULT_BROWSER} #{url}`
end

def private_open(url)
  log("Opening: #{url}")
  `#{DEFAULT_PRIVATE_BROWSER} #{url}`
end

def alt_open(url)
  log("Opening: #{url}")
  `#{ALT_BROWSER} #{url}`
end

def filter_url(url)
  case url
  when *DROP_PARAMS_DOMAINS then drop_params(url)
  when *TRUSTED_DOMAINS then open(url)
  when *ALT_BROWSER_DOMAINS then alt_open(url)
  else
    log("Unknown: #{url}")

    private_open(url)
  end
end

begin
  filter_url ARGV[0]
rescue ::Exception => e
  `echo '#{e}' >> /tmp/custom-open-link`
end
