## Python Flask Moscow timezone Watch

### Repository preparation

```bash
git clone https://github.com/tjann7/DevOps-Course.git
cd DevOps-Course
```

### Dependencies installation

```bash
pip install -r requirements.txt
```

### Starting the app
In terminal of the project ('of the project' means being in the project directory) execute bash command:

        python .\app_python\moscow_app.py

A running server should have an output similar to this image:

![alt text](./images/image.png)
From which a webapp address can be taken. If a general port is not occupied and no permission issues, the address is always http://localhost:5000

Resulting webpage should look like this:

![alt text](./images/image1.png)

## Unit Testing

While being in the repository path, input the following command

```bash
cd app_python
```

Next, simply run python via framework 'unittest':

```bash
python -m unittest tests.py
```

The output, in case of successfullly passed, will be similar to this:

```bash
...
----------------------------------------------------------------------
Ran 2 tests in 0.243s

OK
```

# ENDING

## CI/CD Github Actions
The project has github actions configured to automatically deploy the web-app application when push or pull request to the master branch. 

Settings for workflows:
1.  Navigate to the repository settings: Settings → Secrets → Actions
2.  Create two secrets: `DOCKER_USERNAME` - your Docker login, `DOCKER_PASSWORD` - your Docker login password and `SNYK_TOKEN` - your Snyk api token

