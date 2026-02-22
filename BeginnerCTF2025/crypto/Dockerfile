FROM pwn.red/jail
COPY --from=ubuntu / /srv
RUN mkdir /srv/app

ENV FLAG=mini{d15scr373_10g_15_h4rd_d7c6d0e465cd8ab9}
COPY ./challenge1.py /srv/app/run

