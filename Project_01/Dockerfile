FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y python3-tk && \
    apt-get install -y x11-apps && \
    pip install psutil

WORKDIR /app 

COPY system_monitoring_app.py .

CMD ["python","system_monitoring_app.py"]
