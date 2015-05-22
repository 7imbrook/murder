FROM centos:7

RUN mkdir -p /opt/src
COPY ./ /opt/src

CMD bash
