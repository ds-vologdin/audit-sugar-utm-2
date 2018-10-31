FROM python:3.7-alpine

RUN addgroup -S auditor && adduser -S -G auditor auditor
RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev mariadb-dev

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=auditor:auditor . .

USER auditor:auditor
