FROM gcc:13.3.0@sha256:845328b7cbdbd3cabd015eac5256043aebbea0f9081e74d479d3a2cdd840e6b5 AS builder
WORKDIR /builder/
COPY main.c Makefile ./
RUN make

FROM debian:12.10-slim@sha256:b1211f6d19afd012477bd34fdcabb6b663d680e0f4b0537da6e6b0fd057a3ec3 AS bootstrap
WORKDIR /app/
COPY --from=builder /builder/buffer_overflow_0 ./run

FROM pwn.red/jail:0.4.1@sha256:ee52ad5fd6cfed7fd8ea30b09792a6656045dd015f9bef4edbbfa2c6e672c28c
COPY --from=bootstrap / /srv
COPY flag.txt /srv/app/
