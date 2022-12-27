FROM selenium/standalone-chrome

#ENV user='dXNlcm5hbWU='
#ENV pass='MTIzNDU2'

USER root
RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install selenium==4.1.3

RUN wget https://raw.githubusercontent.com/ylrax/auto_logger/master/autologger_docker.py
#COPY . .

#RUN python3 ./autologger_docker.py $user $pass
RUN python3 ./autologger_docker.py