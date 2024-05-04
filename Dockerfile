FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app/dashboard.py", "--server.port", "8501"]