# Stage 1: Build stage
FROM python:3.10-slim as builder

WORKDIR /app

# Install build dependencies if any (e.g., for compiling C extensions)
# RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app

# Stage 2: Final stage
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /app /app

# Set environment variables if needed (e.g., from Docker Compose)
# ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
