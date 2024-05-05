FROM node:18 AS build

WORKDIR /opt/fvweb/frontend
COPY . .

RUN npm install
RUN npm run build

FROM nginx:1.25.5-alpine AS production

COPY --from=build /opt/fvweb/frontend/dist /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
