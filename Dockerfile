FROM python:3.7.4

RUN pip install --no-cache-dir --upgrade pip pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy

COPY . /app

EXPOSE 8000

CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "--log-level=debug", "phedit.wsgi:application"]