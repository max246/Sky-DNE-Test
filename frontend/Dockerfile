FROM node:latest as build
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package.json /usr/src/app
ENV NODE_OPTIONS=--openssl-legacy-provider

RUN npm install

COPY . /usr/src/app
RUN npm run build

FROM nginx:alpine
CMD ls -la /usr/share/nginx/html 
COPY --from=build /usr/src/app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
