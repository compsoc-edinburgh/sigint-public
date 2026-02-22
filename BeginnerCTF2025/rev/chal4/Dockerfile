FROM pwn.red/jail
COPY --from=ubuntu / /srv
RUN mkdir /srv/app 

COPY chal4 /srv/app/run
COPY flag.txt /srv/flag.txt

