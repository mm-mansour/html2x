FROM frolvlad/alpine-python3

MAINTAINER Mahmoud Mansour

#Firefox is found in testing
RUN sed -i -e 's/v3\.7/edge/g' /etc/apk/repositories && \
    echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories

RUN \
apk update && apk upgrade && \
apk add bash firefox dbus ttf-freefont fontconfig imagemagick msttcorefonts-installer && \
rm -rf /var/cache/apk/*

#Configure Microsoft fonts
RUN update-ms-fonts
RUN fc-cache -f

ADD webservice .

RUN pip install -r requirements.txt

ENV MOZ_HEADLESS=1

CMD ["python", "engine.py"]