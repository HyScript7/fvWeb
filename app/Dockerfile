FROM python
WORKDIR /app
COPY . .
# Install requirements
RUN ["python", "-m", "pip", "install", "-r", "./requirements.txt"]
WORKDIR /app/static/sass/
RUN "./getBootstrap.sh"
WORKDIR /app

# Setup Env
ENV DB_HOST=db
ENV DB_PORT=27017
ENV DB_USER=root
ENV DB_PASS=root
ENV FLASK_DEBUG=False
ENV FLASK_PORT=8080
ENV FVWEB_SESSION_LIFETIME=15
ENV FVWEB_SESSION_SECRET=S3CR37_CH4NG3_M3

# Expose ports
EXPOSE ${FLASK_PORT}

# Run the application
CMD ["python3", "./app.py"]
