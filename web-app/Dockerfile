FROM python:3.9.2

WORKDIR /web-app

ADD . /web-app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
