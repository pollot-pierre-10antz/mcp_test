FROM python:3.13-slim

WORKDIR /app
COPY . .

RUN pip install -U pip && \
    pip install -r requirements.txt --no-cache-dir

EXPOSE 8000
CMD ["python", "main.py"]