
# pull official base image
FROM python:3.7.5

ADD . /app
WORKDIR /app

# set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

# install dependencies
#RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app"]