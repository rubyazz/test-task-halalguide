FROM python:3.10-slim

WORKDIR /app

COPY ../requirements/base.txt requirements/

RUN pip install --no-cache-dir -r requirements/base.txt

COPY .. .

EXPOSE 8000

CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]