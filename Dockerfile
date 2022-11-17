FROM python:3.11.0-slim
RUN pip install gunicorn
COPY simple_web_app /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app
ENV DEBUG=False
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --no-input
CMD gunicorn simple_web_app.wsgi:application --bind "0.0.0.0:8000"
