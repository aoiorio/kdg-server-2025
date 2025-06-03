# ---------python--------
# FROM python:3.9.11

# ENV PYTHONUNBUFFERED 1
# RUN mkdir -p /root/workspace
# COPY requirements.txt /root/workspace/
# WORKDIR /root/workspace

# RUN pip install --upgrade pip\
#     && pip install --upgrade setuptools\
#     && pip install -r requirements.txt

# ImportError Solution:
# 仮想環境内にopencvをinstallする
# LINK: https://qiita.com/siruku6/items/b8aae4cdbf6ebc0dc5d6
# RUN apt -y update
# RUN apt -y install libopencv-dev


# ---------nginx install and run--------
# FROMにはdocker hubで調べられる
# FROM hoge のhogeをタグという
FROM ubuntu:24.04

RUN <<EOF
apt-get update
apt-get install -y nginx
EOF
# FROM ubuntu:24

# RUN apt-get update && \
#     apt-get install -y -q curl gnupg2
# RUN curl http://nginx.org/keys/nginx_signing.key | apt-key add -


# RUN apt-get update && \
#     apt-get install -y -q nginx

# EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]