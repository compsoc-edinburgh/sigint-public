# Copyright 2020 Google LLC
# Modifications copyright 2024 SIGINT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FROM node:18-slim as chroot

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
       curl ca-certificates socat gnupg lsb-release software-properties-common \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .
RUN npm install

FROM gcr.io/kctf-docker/challenge@sha256:0f7d757bcda470c3bbc063606335b915e03795d72ba1d8fdb6f0f9ff3757364f

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends tzdata apache2 \
    && ln -fs /usr/share/zoneinfo/Europe/London /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

RUN service apache2 start

COPY --from=chroot / /chroot

# For Proxy
RUN ln -s /etc/apache2/mods-available/proxy.load /etc/apache2/mods-enabled/
RUN ln -s /etc/apache2/mods-available/proxy_http.load /etc/apache2/mods-enabled/

COPY apache2-kctf-nsjail.conf /etc/apache2/conf-enabled/

COPY web-servers.nsjail.cfg /app/web-servers.nsjail.cfg

VOLUME /var/log/apache2
VOLUME /var/run/apache2

CMD kctf_setup \
    && (kctf_drop_privs nsjail --config /app/web-servers.nsjail.cfg --port 8081 -- /app/nodejs.sh &) \
    && bash -c 'source /etc/apache2/envvars && APACHE_RUN_USER=user APACHE_RUN_GROUP=user /usr/sbin/apache2 -D FOREGROUND'
