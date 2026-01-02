FROM selenium/standalone-chrome

#ENV user='dXNlcm5hbWU='
#ENV pass='MTIzNDU2'

USER root
RUN apt-get update && apt-get install python3-setuptools -y
# for the future me. perhaps better use pipx
RUN apt-get update && apt-get install python3-pip -y

WORKDIR /app
COPY requirements.txt .
COPY autologger_docker.py .
#RUN wget https://raw.githubusercontent.com/ylrax/auto_logger/master/autologger_docker.py
#RUN wget https://raw.githubusercontent.com/ylrax/auto_logger/master/requirements.txt

RUN pip3 install -r requirements.txt --break-system-package
#COPY . .

#RUN python3 ./autologger_docker.py $user $pass
CMD ["python3", "./app/autologger_docker.py"]