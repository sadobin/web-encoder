FROM ubuntu

RUN     apt update && \
        apt install -y python3.8 && \
        apt install -y python3-pip && \
	pip3 install django

RUN     mkdir /opt/app

COPY . /opt/app

WORKDIR /opt/app

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:80"]
