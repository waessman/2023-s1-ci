# A project to support continuous integration classes

## Problem Statement
This repository implements a HTTP API to validate a password text according to
some criteria. But it is incomplete and has bugs, it is your job to fix it and complete the code.<br>

It was developed using **poetry** package manager, but we have included the 
_requirements.txt_ and _requirements-dev.txt_ to help who doesn't. Refer to 
_requirements-dev.txt_ to the development environment dependencies and to 
_requirements.txt_ to just the web app dependencies.

### Passwords must comply to:
1. 8 characters minimum<br>
2. At least 1 number<br>
3. At least 1 especial character<br>
4. At least 1 upper case letter<br>
5. At least 1 lower case letter<br>
6. Especial characters can not be / ^ ~<br>

# Tasks
## 0. Fork the project on gitlab; 
## 1. Verify that tests don't cover your specification and code proper tests;
## 2. Fix any bugs that you find;
## 3. The ci pipeline seems messed up, fix it.

# Installing the development environment

[![asciicast](https://asciinema.org/a/538713.svg)](https://asciinema.org/a/538713)
## Development environment dependencies
| Dependencies      | Tested Version | Minimum Version | Url                                                            |
|-------------------|----------------|-----------------|----------------------------------------------------------------|
| Python            | 3.11           | 3.7.5           | [link](https://www.python.org/downloads/release/python-3110/)  |
| Poetry (optional) | 1.2.0          | 1.0.0           | [link](https://python-poetry.org/)                             |

### clone the project
````shell
$ git clone ssh://git@gitlab.ic.unicamp.br:2222/ra220102/mc426-2022-s2-ci.git
````

### when using poetry just install dependencies and enter the virtual environment
````shell
$ cd mc426-2022-s2-ci
$ poetry install
$ poetry shell
````

### when **NOT** using poetry install dependencies from the inner requirements.txt
It is advisable to use a virtual environment
````shell
$ cd mc426-2022-s2-ci/simple_web_app
$ pip install -r requirements.txt
````

## Running the web app
### running from code
````shell
$ cd mc426-2022-s2-ci/simple_web_app
$ uvicorn main:app --reload
````

### running from docker
````shell
$ cd mc426-2022-s2-ci
$ docker build -t simple_web_app .
$ docker run --rm -p 8000:80 simple_web_app
````

## Running the tests
````shell
$ cd mc426-2022-s2-ci
$ pytest
````
