FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.pip /config/
RUN apk update \
 && apk add --no-cache
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade setuptools
RUN pip install -r /config/requirements.pip
RUN mkdir /src;
WORKDIR /src
