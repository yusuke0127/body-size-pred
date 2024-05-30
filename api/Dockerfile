# api/Dockerfile

FROM python:3.10.6-slim

WORKDIR /api

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# # Use this when running locally
# EXPOSE 8080

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

# Use this when deploying to GCP
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
