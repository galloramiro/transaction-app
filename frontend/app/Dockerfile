FROM node:12.2.0-alpine as build

RUN mkdir /app
WORKDIR /app

COPY ./frontend/app/package.json /app/
RUN npm install --slient
RUN npm install @material-ui/core

COPY ./frontend/app/ /app/

EXPOSE 3000
