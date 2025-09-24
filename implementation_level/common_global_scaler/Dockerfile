FROM python:3.11

WORKDIR /app

# Install Pulumi (bundled YAML plugin included)
RUN curl -fsSL https://get.pulumi.com | sh

# Add Pulumi to PATH
ENV PATH=/root/.pulumi/bin:$PATH

# Pulumi backend directory
RUN mkdir -p /app/pulumi-backend
ENV PULUMI_BACKEND_URL=file:///app/pulumi-backend
ENV PULUMI_CONFIG_PASSPHRASE=""

# Copy source and requirements
COPY src ./src
COPY requirements.txt ./

# Install Python dependencies
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=0

# Default command
CMD ["python", "./src/main.py"]
