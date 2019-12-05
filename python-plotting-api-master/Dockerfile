FROM python:3.7-stretch
ADD . /app
WORKDIR /app
ARG run_env

RUN pip install --no-cache-dir --trusted-host pypi.python.org pipenv

RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt
ENV run_env=$run_env

CMD gunicorn -b 0.0.0.0:$PORT --chdir python_plotting_api app:app --pythonpath .