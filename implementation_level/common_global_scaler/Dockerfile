FROM python:3.11

WORKDIR /app

RUN curl -fsSL https://get.pulumi.com | sh && \
    mv /root/.pulumi/bin/pulumi /usr/local/bin/

COPY src ./src

COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=0
CMD ["python", "./src/main.py"]

