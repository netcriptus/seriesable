#!/bin/sh

curl db:5432 >&- 2>&-
while [[ $? != 52 ]]; do
  sleep 2
  curl db:5432 >&- 2>&-
done

python /code/manage.py migrate && \
python /code/manage.py runserver 0.0.0.0:8000
#celery -A seriesable worker -l info
