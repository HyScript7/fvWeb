
# fvWeb

Flask application for the Fusionverse website, licensed under the MIT license.

## Requirements

- Python 3.10.X (Module requirements are in app/requirements.txt)
- MongoDB
- Redis
- NGINX (for load balancing across multiple application instances)

## Setup

### Bare metal

To run the application, you must first install all the requirements (and dependencies) above.  
You will need to setup a Mongo database and Redis database to use with the application.  
You can run any number of the flask app instances using waitress, even on separate hosts, as long as the env file remains the same across all of them.
Lastly you want to setup nginx as a load balancer for the applications. (This is the service we will be connecting to from our browser)

### Docker

There is a Dockerfile and docker-compose file provided, as well as the Redis configuration file.  
The simplest setup can be done by running `docker-compose up -d`
