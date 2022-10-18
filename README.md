
# Fusionverse Web

## About

This is the Fusionverse Web & API Repository
Although using Bootstrap, it is not included in the source code by default, there is a download script instead. It is ment to be ran when building the image or running from source for the first time.

## Running

### Setup Guide for Running from Source

1) Install python 3.9+
2) Install requirements using `pip install -r ./app/requirements.txt`
3) Change directory into /app/ or open a new terminal inside the folder
4) Setup a MongoDB server
5) Edit .env to match your settings
6) cd into /static/sass and run the getBootstrap.sh script or getBootstrap.ps1 if you're using powershell.
7) cd back into /app/ and run `python ./app.py`

### Running Using Docker or Docker Compose

#### Building the Docker Image

To Build the Docker Image of fvWeb for use with `docker run`, use the commands below:

```bash
cd app
docker build -t fvweb:latest .
```

You will now have a new image called `fvweb:latest` that can be ran.
**You do not need to build the image if you're using docker-compose, as it will build the image once you run the compose command**

#### Using Docker Compose

Create a docker-compose.yml file or use the template below:

```yml
version: "3.9"
services:
  web:
    build: ./app
    restart: always
    ports:
    - 8080:8080
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
  dbadmin:
    image: mongo-express
    restart: always
    ports:
    - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ENABLE_ADMIN: true
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: root
      ME_CONFIG_MONGODB_SERVER: db
      ME_CONFIG_OPTIONS_EDITORTHEME: ayu-dark
```

Create a new instance of fvWeb using the command below

```bash
docker-compose -d up
```

To stop and delete the instance of fvWeb, run the following command

```bash
docker-compose down
```

**You do not need to build the image if you're using docker-compose, as it will build the image once you run the compose command**

## License & Copyright

Copyright (c) 2022 HyScript7
fvWeb (Fusionverse Web) is licensed under the MIT License
