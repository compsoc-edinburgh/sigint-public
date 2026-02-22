FROM node:20-alpine
WORKDIR /app

RUN apk add --no-cache chromium

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

# debug install and run tree
RUN npm install -g tree
RUN tree .


EXPOSE 3001

CMD ["npm", "run", "start"]