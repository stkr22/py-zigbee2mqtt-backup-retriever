FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

COPY src /app/
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir wheel \
    && pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["python3", "/app/zigbee2mqtt_backup_retriever.py"]
