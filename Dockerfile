FROM python
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

ADD . /app/

COPY requirements.txt /app/
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:80


