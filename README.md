# auto_logger
Selenium web autologger for minijuegos with python 3 and selenium

### Requirements:

- Selenium
- Chrome driver installed

### Usage

Both parameters must be base64 encoded

    python autologger.py <username> <password>

### docker usage

Compile and create the image in the project folder, for example chromium with the tag v1

    docker build -t chromium:v1 .

Execute the container:

    docker run -it chromium:v1 /bin/bash

Or directly the python script:

    docker run -it chromium:v1 python3 autologger_docker.py <username> <password>


#### Internal testing

Habilitate the coments of picture to check the steps

    sudo docker ps

    docker cp 2873:/test.png ~/repos/cachareo/docker_files2/test.png