FROM selenium/standalone-chrome

USER root
RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install selenium==4.1.3

RUN wget https://github.com/ylrax/auto_logger/blob/master/autologger_docker.py
#COPY . .
