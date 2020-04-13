FROM node:12.2.0-alpine as build

RUN mkdir /app
WORKDIR /app

COPY package.json /app
RUN npm install

COPY . /app/

EXPOSE 3000
CMD ["npm", "start"]
