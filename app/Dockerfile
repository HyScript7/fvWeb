FROM python
COPY . .
RUN ["python", "-m", "pip", "install", "-r", "./requirements.txt"]
EXPOSE 5000
CMD ["python3", "-m", "flask", "run"]