
# Fusionverse Web

## About

This is the Fusionverse Web & API Repository

## Docker & Docker Compose

Building the fvWeb Image:

```bash
cd app
docker build -t fvweb:latest .
```

Using docker-compose:

```yml
version: "3.9"
services:
  web:
    build: ./app
    restart: always
    ports:
    - 5000:5000
  db:
    image: mongo
    restart: always
    ports:
    - 27017:27017
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: root

```

```bash
docker-compose -d up
```

The docker compose file will automatically build the image, so you don't have to build it manually.
