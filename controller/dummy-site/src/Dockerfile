FROM python:alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir kopf requests

EXPOSE 8080

CMD ["kopf", "run", "--standalone", "crd-controller.py"]
