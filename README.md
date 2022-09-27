
# Fusionverse Web

## About

This is the Fusionverse Web & API Repository

## Running

Running from source

1) Install python 3.9
2) Install requirements using `pip install -r ./app/requirements.txt`
3) Change directory into /app/ or open a new terminal inside the folder
4) Setup a MongoDB server
5) Edit .env to match your settings
6) cd into /static/sass and run the getBootstrap.sh script or getBootstrap.ps1 if you're using powershell.
7) cd back into /app/ and run `python ./app.py`

## Using Docker & Docker Compose

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
    - 8000:8000
    environment:
      DB_HOST: db
      DB_PORT: 27017
      DB_USER: root
      DB_PASS: root
      FLASK_DEBUG: False
      FLASK_PORT: 8080
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
