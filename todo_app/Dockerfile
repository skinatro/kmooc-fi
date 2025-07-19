FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=9000

EXPOSE 5000

CMD ["python","-u","./webserver.py"]