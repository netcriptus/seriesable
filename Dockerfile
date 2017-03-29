FROM jormar/python3.6-alpine
RUN apk add postgresql-dev gcc musl-dev curl
COPY . /code
RUN pip3 install -r /code/requirements.txt
ENTRYPOINT ["/code/entrypoint.sh"]
