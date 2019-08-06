FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip install -r requirements.txt
COPY app.py .
COPY requirements.txt requirements.txt
CMD ["flask", "run"]