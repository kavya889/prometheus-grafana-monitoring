# Dockerfile

FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Bandit and Pytest
RUN pip install --no-cache-dir bandit pytest

# Add Bandit config
COPY bandit.yml /app/bandit.yml

# Copy your project files
COPY . /app

WORKDIR /app

# Run Bandit and Pytest
CMD ["bash", "-c", "bandit -r . -f html -o bandit_report.html; pytest || true"]
