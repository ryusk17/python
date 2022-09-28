# 3.x のように小数点以下を指定しない場合、安定版3.xとなる?
FROM python:3

# USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# TODO 最低限のdotfileのコピー
# COPY .bashrc
# COPY .vimrc

# rootではないユーザー作成 ※Dockerfile末尾に記載すること、apt-getはroot権限で実行
ARG USERNAME=user
ARG GROUPNAME=user
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME
USER $USERNAME
# WORKDIR /home/$USERNAME/ # docker-compose.yml で指定
