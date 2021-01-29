FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /lenme
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /lenme/
RUN pip install -r requirements.txt
COPY . /lenme

ENTRYPOINT ["/lenme/entrypoint.sh"]