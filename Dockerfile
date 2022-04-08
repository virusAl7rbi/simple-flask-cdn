from python:3.9.7-alpine3.14

copy . /app
workdir /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

run pip3 install -U pip
run pip3 install flask gunicorn
EXPOSE 30
CMD chmod +x gunicorn.sh && ./gunicorn.sh
