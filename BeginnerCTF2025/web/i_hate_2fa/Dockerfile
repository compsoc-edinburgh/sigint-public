FROM ghcr.io/puppeteer/puppeteer:latest

WORKDIR /app

COPY package.json /app/package.json
RUN npm install

COPY views/ /app/views/
COPY public/ /app/public/
COPY bot.js /app/bot.js
COPY server.js /app/server.js


CMD ["node", "server.js"]
EXPOSE 3000