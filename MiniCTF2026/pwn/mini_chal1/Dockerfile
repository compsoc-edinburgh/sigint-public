FROM pwn.red/jail
COPY --from=ubuntu / /srv
RUN mkdir /srv/app 

COPY chal1 /srv/app/run
COPY flag.txt /srv/app/flag.txt

