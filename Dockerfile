FROM alpine:edge
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
# RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk update
RUN apk add --no-cache python3 py3-flask
ADD a.py /a.py
EXPOSE 4040

ENTRYPOINT python3 /a.py
