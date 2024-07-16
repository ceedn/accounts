FROM python:3.8

WORKDIR /app

COPY requirements.txt /app
COPY acm/ /app

RUN pip install uvicorn
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]