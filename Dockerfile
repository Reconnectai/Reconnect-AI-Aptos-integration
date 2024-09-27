ARG  DOCKER_PYTHON_IMAGE=python:3.11.0-slim
FROM $DOCKER_PYTHON_IMAGE AS reconnect_aptos_auth

WORKDIR /app

COPY sections /app/sections
COPY app.py blueprints.py config.py dto.py /app/
COPY Pipfile Pipfile.lock* /app/
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile --${PIPENV_ARGS}
RUN pipenv update

RUN cat /etc/ssl/certs/ca-certificates.crt >> `python -m certifi`

ENV PYTHONPATH=.

EXPOSE 8090
ENTRYPOINT ["python", "-m", "pipenv", "run", "python", "app.py"]
