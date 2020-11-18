FROM ubuntu:20.04

RUN apt-get update

RUN apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

RUN apt-get update
RUN apt-get install -y docker-ce docker-ce-cli containerd.io


RUN bash service docker start
VOLUME /var/run/docker.sock:/var/run/docker.sock

RUN docker build -t openalpr https://github.com/openalpr/openalpr.git

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN mkdir -p /var/www/uploads
RUN mkdir -p /app

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN chmod +x bootstrap.sh

CMD ["bootstrap.sh"]
EXPOSE 5000