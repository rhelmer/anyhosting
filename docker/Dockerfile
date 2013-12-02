FROM ubuntu:quantal

# FIXME see https://github.com/dotcloud/docker/issues/1024
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -s /bin/true /sbin/initctl

RUN apt-get update
RUN apt-get install -y mysql-server libapache2-mod-php5 phpmyadmin

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80:8080 22

CMD ["/usr/bin/supervisord"]
