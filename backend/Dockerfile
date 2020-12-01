#Set Python Version
FROM python:latest
#Set Direct
WORKDIR /api

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "debug.py"]
