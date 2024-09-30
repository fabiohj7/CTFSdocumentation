FROM crystallang/crystal:1.8.2 AS crystal
RUN apt install git
RUN apt update && apt install -y python3
WORKDIR /tmp
RUN git clone https://github.com/cosmo-lang/cosmo
WORKDIR /tmp/cosmo
RUN make install

FROM pwn.red/jail

COPY --from=crystal / /srv

RUN mkdir /srv/app
COPY run.sh /srv/app/run
COPY jail.py /srv/app/jail.py
COPY flag.txt /srv/app/flag.txt

ENV JAIL_MEM=20M JAIL_TIME=30 JAIL_PIDS=8 JAIL_CONNS_PER_IP=3 JAIL_CONNS=23