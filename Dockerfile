FROM python:3.13.2-bookworm
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000
CMD ["gunicorn", "--config", "gunicorn_config.py", "babytracker.manage:gunicorn_app"]
