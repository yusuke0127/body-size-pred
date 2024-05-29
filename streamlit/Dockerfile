# streamlit/Dockerfile
FROM python:3.10.6-slim

WORKDIR /streamlit

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
