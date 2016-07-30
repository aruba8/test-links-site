FROM python:3.5
MAINTAINER Erik Khalimov <erik.khalimov@me.com>
RUN apt-get update && apt-get install -y curl vim nano 
WORKDIR /application
ADD application /application
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python run.py