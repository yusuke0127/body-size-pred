# streamlit/Dockerfile
FROM python:3.10.6-slim

WORKDIR /streamlit

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# When deploying to GCP
CMD streamlit run --server.port $PORT main.py

# Uncomment the lines below when developing locally
# EXPOSE 8501

# CMD ["streamlit", "run", "main.py"]
