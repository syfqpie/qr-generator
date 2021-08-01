FROM python:3.9

RUN apt update
RUN apt install nano

ADD . /app
# COPY ./gunicorn-config.py gunicorn-config.py

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app

EXPOSE 6100
CMD ["uvicorn", "main:app", "--reload"]
# CMD ["gunicorn", "app.main:app", "--config=gunicorn-config.py"]