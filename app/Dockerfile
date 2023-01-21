FROM python:3.10.9

WORKDIR /app
COPY . .

# Install requirements
RUN ["pip", "install", "--upgrade", "pip"]
RUN ["python", "-m", "pip", "install", "-r", "./requirements.txt"]
RUN ["./getDependencies.sh"]

# Setup Env
ENV FLASK_SECRET=CH4NG3_M3
ENV FLASK_SESSION_LIFETIME=15
ENV FLASK_PORT=5000
ENV FLASK_DEBUG=true
ENV MONGO_HOST=localhost
ENV MONGO_PORT=27017
ENV MONGO_USER=root
ENV MONGO_PASS=root
ENV MONGO_SRV=false
ENV REDIS_HOST=localhost
ENV REDIS_PORT=6379
ENV REDIS_PASS=root
ENV FVWEB_DATABASE=fvWeb
ENV FVWEB_USERS=Accounts
ENV FVWEB_ARTICLES=Articles
ENV FVWEB_DISCUSSIONS=Discussions

# Expose ports
EXPOSE ${FLASK_PORT}

# Run the application
CMD ["python3", "./main.py"]
