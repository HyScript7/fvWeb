FROM python:3.11.8 AS pre

WORKDIR /opt/fvweb

RUN python -m pip install poetry

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry export --without-hashes --format requirements.txt --output requirements.txt

FROM python:3.11.8 AS prod

WORKDIR /opt/fvweb

COPY --from=pre /opt/fvweb/requirements.txt .
COPY app ./app

RUN python -m pip install --no-cache-dir --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt

RUN rm requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
