FROM python:3.7-alpine
WORKDIR /code
COPY app.py .
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["flask", "run"]