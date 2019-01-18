FROM ubuntu:17.10

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python3 python-dev python3-pip python-virtualenv libpq-dev
RUN update-alternatives --remove python /usr/bin/python2.7

# Setup flask application
RUN mkdir -p /opt/app
COPY . /opt/app
RUN pip3 install -r /opt/app/requirements.txt
RUN pip3 install --no-cache-dir --ignore-installed --no-binary :all: psycopg2
WORKDIR /opt/app

EXPOSE 5000

RUN chmod +x /opt/app/run.sh
CMD ["/opt/app/run.sh"]