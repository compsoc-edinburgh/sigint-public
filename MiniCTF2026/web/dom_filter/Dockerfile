FROM ghcr.io/puppeteer/puppeteer:latest
WORKDIR /app

COPY app.js /app/app.js
COPY bot.js /app/bot.js
COPY package.json /app/package.json

RUN npm install

CMD [ "node", "app.js" ]

EXPOSE 5000