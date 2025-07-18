FROM python:3-slim

WORKDIR /usr/src/app

COPY . .

ENV PORT=5001

RUN pip install -r requirements.txt

CMD ["python","-u","./log_output.py"]