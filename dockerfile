FROM selenium/standalone-chrome

#ENV user='dXNlcm5hbWU='
#ENV pass='MTIzNDU2'

USER root
RUN apt-get update && apt-get install python3-setuptools -y
RUN apt-get update && apt-get install python3-pip -y
RUN pip3 install selenium==4.1.3 --break-system-package

RUN wget https://raw.githubusercontent.com/ylrax/auto_logger/master/autologger_docker.py
#COPY . .

#RUN python3 ./autologger_docker.py $user $pass
CMD python3 ./autologger_docker.py