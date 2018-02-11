FROM debian:stretch


RUN apt-get update \
    && apt-get install -y \
    apt-utils git wget nano \
    python3 python3-pip
RUN apt-get install -y --no-install-recommends \
    zlib1g-dev libjpeg-dev

#RUN mkdir /var/instaforex \
#    && cd /var/instaforex \
#    && git clone https://github.com/ytec/instaforex-web.git \
#    && pip3 install -r /var/instaforex/instaforex-web/requirements.txt

RUN mkdir /var/instaforex
COPY ./ /var/instaforex
RUN pip3 install -r /var/instaforex/requirements.txt
WORKDIR /var/instaforex
#CMD python3 /var/instaforex/manage.py runserver
EXPOSE 8000
