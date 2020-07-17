FROM python:3.8-slim-buster
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "debug.py"]