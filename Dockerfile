FROM python:3.9-slim
# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY flaskr/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#CMD pytest -v
CMD python -m flask run --host=0.0.0.0