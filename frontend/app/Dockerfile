FROM node:12.2.0-alpine as build

RUN mkdir /app
WORKDIR /app

COPY package.json /app/
RUN npm install --slient
RUN npm install @material-ui/core

COPY . /app/

EXPOSE 3000
