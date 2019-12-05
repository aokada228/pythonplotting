# Python Plotting API

Using Matplotlib, Seaborn, Pandas and Flask to expose scientific plots through APIs. 

## What is this about

This repo shows an option to share your plots with other through a webservice interface.
No need of complex tool setup or anythin else, just plain python.

## How to run the repo

### Run from localhost
```
pip install --no-cache-dir --trusted-host pypi.python.org pipenv
pipenv instal --dev
pipenv run py.test
PYTHONPATH=. pipenv run python python_plotting_api/app.py
``` 

### Run via docker

```
docker build --build-arg run_env=dev . -t pythonplotting:test
docker run -e PORT=5000 -p 5000:5000 pythonplotting:test
```


## Deployment

This app is containerized and deployed to Heroku and reachable under:

https://python-sci-plotting.herokuapp.com/