## Python Flask Moscow timezone Watch

![Python CI](https://github.com/IlsiyaNasibullina/S25-core-course-labs/actions/workflows/app_python.yml/badge.svg)

## Repository preparation

```bash
git clone https://github.com/tjann7/DevOps-Course.git
cd DevOps-Course
```

## Dependencies installation

```bash
pip install -r requirements.txt
```

## Starting the app
In terminal of the project ('of the project' means being in the project directory) execute bash command:

        python .\app_python\moscow_app.py

A running server should have an output similar to this image:

![alt text](./images/image.png)
From which a webapp address can be taken. If a general port is not occupied and no permission issues, the address is always http://localhost:5000

Resulting webpage should look like this:

![alt text](./images/image1.png)

## Docker

Building the image:
```bash
docker build -t your_image_name .
```

Output should be similar to this:
![](images/image_docker1.png)

Pulling the image:
```bash
docker pull tjann7/moscow_time
```

Running the image locally ~~if you don't like parameters, good luck finding container's address~~:
```bash
docker run --network="host" moscow_time
```

Result of running is as follows:

![](images/image_docker2.png)

## Docker-Compose

Alternatively, the webapp can be executed via docker-compose command-line:
```bash
tjann@fedora:~/DevOps-Course/app_python$ docker-compose up -d
WARN[0000] /home/tjann/DevOps-Course/app_python/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 2/2
 ✔ Network app_python_default          Created                                                                                                  0.3s 
 ✔ Container app_python-moscow_time-1  Started                                                                                                  0.7s 
tjann@fedora:~/DevOps-Course/app_python$ 
```

Afterwards, you may observe the address and all the request data in the docker logs:
```bash
tjann@fedora:~/DevOps-Course/app_python$ docker logs app_python-moscow_time-1 
 * Serving Flask app 'moscow_app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.0.2:5000
Press CTRL+C to quit
Requests Counter updated: 8
172.18.0.1 - - [28/Apr/2025 12:02:50] "GET / HTTP/1.1" 200 -
Requests Counter updated: 9
172.18.0.1 - - [28/Apr/2025 12:02:51] "GET / HTTP/1.1" 200 -
Requests Counter updated: 10
172.18.0.1 - - [28/Apr/2025 12:02:51] "GET / HTTP/1.1" 200 -
Requests Counter updated: 11
172.18.0.1 - - [28/Apr/2025 12:02:52] "GET / HTTP/1.1" 200 -
Requests Counter updated: 12
172.18.0.1 - - [28/Apr/2025 12:02:52] "GET / HTTP/1.1" 200 -
tjann@fedora:~/DevOps-Course/app_python$ 
```

## Request Counter(Lab12)

Within __app_python directory__ we now have a mounted volume __./data__ for storing Total Request Counter file:
```bash
tjann@fedora:~/DevOps-Course/app_python$ tree .
.
├── CI.md
├── data
│   └── visits
├── docker-compose.yml
├── Dockerfile
...
```

## Running unittest

While being in the repository's directory, input the following commands:

```bash
cd app_python
python -m unittest tests.py
```
This runs a few commands to check that the webapp works properly. In case of successful passing, the result should be similar to this:

```bash
...
----------------------------------------------------------------------
Ran 3 tests in 0.004s

OK
```

## CI Workflow

The workflow is configured to automate the following stages:

* Dependencies - using requerements.txt
* Lint - Checking coding conventions (line length, etc.)
* Snyk - Checks for security vulnerabilities.
* Test - tests.py unittest is called to verify functionality
* Docker - Builds and pushes the Docker image to Docker Hub.

