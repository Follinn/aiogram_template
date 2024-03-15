FROM python:3.10.11
LABEL authors="Follin"

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt
CMD ["python",  "main.py"]