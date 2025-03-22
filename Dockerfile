FROM python:3.11-slim


WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
