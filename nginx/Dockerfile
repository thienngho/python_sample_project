FROM nginx:latest

MAINTAINER thienho

RUN rm -f /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/

COPY web.conf /etc/nginx/conf.d
