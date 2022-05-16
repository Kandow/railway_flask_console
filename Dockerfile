FROM alpine:edge
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
# RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk update
RUN apk add --no-cache supervisor bash openssh wget
RUN wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
RUN tar -xzf ngrok-v3-stable-linux-amd64.tgz -C /bin
RUN chmod +x /bin/ngrok
RUN ngrok config add-authtoken 29E4uENoarQdDJnURKX4QOYwOy0_4KF3ECuzviifRGJKKWmKi
RUN echo 'web_addr: 0.0.0.0:4040' >> /root/.config/ngrok/ngrok.yml 
RUN ssh-keygen -A
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN echo 'root:admin' | chpasswd
ADD supervisord.conf /etc/supervisord.conf

ADD entry.sh /entry.sh

RUN chmod +x /entry.sh


EXPOSE 4040

ENTRYPOINT ["/bin/bash", "-c", "/entry.sh"]
