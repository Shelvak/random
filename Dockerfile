FROM node:14-buster-slim

RUN apt update && \
    apt install -y git make build-essential openssl tzdata lib32z1 lib32z1-dev \
                   zlib1g zlib1g-dev ca-certificates curl wget gnupg zstd vim bash \
                   bzip2 libffi-dev libgmp-dev libssl-dev libyaml-dev procps

ENV LANG C.UTF-8
ENV GEM_HOME /usr/local/bundle
ENV BUNDLE_SILENCE_ROOT_WARNING=1
ENV BUNDLE_APP_CONFIG="$GEM_HOME"
ENV BUNDLE_BIN="$GEM_HOME/bin"
ENV PATH $GEM_HOME/bin:$PATH
ENV PATH $BUNDLE_BIN:$PATH

RUN echo "$BUNDLE_BIN" && \
    mkdir -p "$BUNDLE_BIN" && \
    chmod 777 "$BUNDLE_BIN" && \
    echo "gem: --no-rdoc --no-ri" >> ~/.gemrc

RUN apt install -y ruby python
RUN curl --compressed -o- -L https://yarnpkg.com/install.sh | bash && \
    npm install --global solc@0.8.4 && \
    gem install bundler

RUN apt autoremove && apt clean && apt autoclean

CMD "bash"
