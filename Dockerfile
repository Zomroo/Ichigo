FROM debian:11
FROM python:3.10.4-slim-buster

WORKDIR /SiestaRobot/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install git
RUN apt-get install ffmpeg -y
RUN apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev python3-pip

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
CMD ["python3.10", "-m", "SiestaRobot"]
