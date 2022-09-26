FROM python
WORKDIR /app
COPY . .
RUN ["python", "-m", "pip", "install", "-r", "./requirements.txt"]
ENV DB_HOST=db
ENV DB_PORT=27017
ENV DB_USER=root
ENV DB_PASS=6nUwMUy1kM4fcrQp
ENV FLASK_DEBUG=false

EXPOSE 5000
CMD ["python3", "-m", "flask", "run"]