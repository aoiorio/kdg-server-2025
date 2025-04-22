FROM python:3.9.11

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /root/workspace
COPY requirements.txt /root/workspace/
WORKDIR /root/workspace

RUN pip install --upgrade pip\
    && pip install --upgrade setuptools\
    && pip install -r requirements.txt

# ImportError Solution:
# 仮想環境内にopencvをinstallする
# LINK: https://qiita.com/siruku6/items/b8aae4cdbf6ebc0dc5d6
RUN apt -y update
RUN apt -y install libopencv-dev