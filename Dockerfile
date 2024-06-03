FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY stix2arango/requirements.txt ./stix2arango-requirements.txt
RUN pip install -r requirements.txt
RUN pip install -r stix2arango-requirements.txt