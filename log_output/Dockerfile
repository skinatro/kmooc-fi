FROM python:3-slim

WORKDIR /usr/src/app

COPY . .

ENV PORT=5000

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python","-u","./log_output.py"]