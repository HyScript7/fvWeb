
# Fusionverse Web

## About
This is the Fusionverse Web (fvWeb) and Fusionverse REST API (fvREST) repository.

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
  app:
    build: ./app
    ports:
    - 5000:5000
```

```bash
docker-compose -d up
```

The docker compose file will automaticaly build the image, so you don't have to build it manually.