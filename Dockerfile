FROM python:3.6.0

RUN mkdir -p /project/run
WORKDIR /project/run
COPY . /project/run
RUN pip install -e .
