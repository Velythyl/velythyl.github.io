FROM jekyll/jekyll:3.8
ARG gems
RUN gem install $gems
