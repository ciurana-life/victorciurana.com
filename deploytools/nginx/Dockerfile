# Pull base image (compiled on M1 arm64 --> x86_64 [uname -m])
FROM --platform=linux/x86-64 jwilder/nginx-proxy
COPY vhost.d/default /etc/nginx/vhost.d/default
COPY custom.conf /etc/nginx/conf.d/custom.conf