FROM python:3.8.10

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0", "--port=5000"]
