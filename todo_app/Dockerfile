FROM python:3-slim

WORKDIR /usr/src/app

RUN mkdir -p ./static

COPY . .

RUN pip install -r requirements.txt

ENV PORT=5000

ENV TIMEOUT=3600

EXPOSE 5000

CMD ["python","-u","./webserver.py"]