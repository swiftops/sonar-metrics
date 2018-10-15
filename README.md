# GET SONARQUBE METRICS MICROSERVICE

### Introduction

* SonarQube (formerly Sonar)[1] is an open source platform developed by SonarSource for continuous inspection of code quality to perform automatic reviews with 
static analysis of code to detect bugs, code smells, and security vulnerabilities on 20+ programming languages. SonarQube offers reports on duplicated code, coding standards, 
unit tests, code coverage, code complexity, comments, bugs, and security vulnerabilities
* This particular service helps us to get the above mentioned sonar metrics in json format
* To get more details about SONARQUBE. Refer [INTRO to SONAR] (https://www.sonarqube.org/)

## service apis :
* GET_SONAR_METRICS

### Pre-Requisite

1. python 3.6.0 or above version.
2. docker (optional) Refer [Install Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04) documentation.
3.Assuming Sonarqube server is up and running with appropriate scanned results inside docker container

# Steps to start sonarqube server and sonar scanner:
* To start sonarqube sever inside docker container : 
```
docker run -it --name sonarqube -p 9000:9000 sonarqube
```
* check  for sonarqube containers ip using docker inspect command and substitute in below command (host.url)
* To start sonarqube scanner inside docker container :
```
docker run -ti -v /path/of/sourcode/to/mount/inside/container:/root/src --link sonarqube --name sonartesting newtmitch/sonar-scanner sonar-scanner -Dsonar.host.url=http://sonar server container ip:port -Dsonar.projectBaseDir=/root/src -Dsonar.projectKey=MySALMCORE -Dsonar.projectName="My SALM Name" -Dsonar.java.binaries=/root/src/externaljars -Dsonar.java.libraries=/root/src/externaljars -Dsonar.sources=/root/src/sourcecode,/root/src/webui
-DSONAR_SCANNER_OPTS="-Xmx2048mx"
```

### Checkout Repository
```
$git clone https://github.com/swiftops/SONAR-METRICS.git
```
### Configuration

##### Steps to start microservice
Once done with the pre-requisite exceute below command to start  microservice
```
docker build -t <image-name>
docker run -p 7975:7975 --name sonarfilterservice  -d <image-name>
```

### How to use
In order to call above microservices. we just need to hit below URL  from the browser
```
http://<MACHINE-IP>/sonarfilterservice/sonarfilter
```
* NOTE : Input should be in the format eg:{ sonar ProjectKey;$ACTUAL_PROJECT_KEY_VALUE}

### On Commit Auto-deploy on specific server.
---
To autodeploy your docker container based service on server used below steps
* You need to configure Gitlab Runner to execute Gitlab CI/CD Pipeline. See [Gitlab Config](https://docs.gitlab.com/runner/install)
<Configure .gitlab-ci.yml and deploy.sh as per your need and remove this line>

As soon as you configure runner auto deployment will start as you commited the code in repository.
refer .gitlab-ci.yml file.

### Deploy on local environment.
----
 
#### Create Virtual Environment
Virtualenv is the easiest and recommended way to configure a custom Python environment for your services.
To install virtualenv execute below command:
```sh
$pip3 install virtualenv
```
You can check version for virtual environment version by typing below command:
```sh
$virtualenv --version
```
Create a virtual environment for a project:
```
$ cd <my_project_folder>
$ virtualenv virtenv
```
virtualenv `virtenv` will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. The name of the virtual environment (in this case, it was `virtenv`) can be anything; omitting the name will place the files in the current directory instead.

This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named `virtenv`.

You can also use the Python interpreter of your choice (like python3.6).
```
$virtualenv -p /usr/bin/python3.6 virtenv
```
To begin using the virtual environment, it needs to be activated:
```
$ source virtenv/bin/activate
```
The name of the current virtual environment will now appear on the left of the prompt (e.g. (virtenv)Your-Computer:your_project UserName$) to let you know that it’s active. From now on, any package that you install using pip will be placed in the virtenv folder, isolated from the global Python installation. You can add python packages needed in your microservice decelopment within virtualenv. 

#### Install python module dependanceies
```
pip install -r requirements.txt
```
#### To start microservice 
```
python services.py
```


#### To access Microservice
```
e.g http://<MACHINE-IP>/sonarfilterservice/sonarfilter
```

### Architechture
![Scheme](perfservice.JPG)


##### Flask
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself.
http://flask.pocoo.org/docs/1.0/quickstart/


##### Gunicorn
The Gunicorn "Green Unicorn" (pronounced gee-unicorn)[2] is a Python Web Server Gateway Interface (WSGI) HTTP server. 

###### Features
* Natively supports [WSGI] (https://wsgi.readthedocs.io/en/latest/what.html) , [web2py] (http://www.web2py.com/) and [Django] (https://www.djangoproject.com/)
* Automatic worker process management
* Simple Python configuration
* Multiple worker configurations
* Various server hooks for extensibility
* Compatible with Python 2.6+ and Python 3.2+[4]
http://docs.gunicorn.org/en/stable/configure.html
