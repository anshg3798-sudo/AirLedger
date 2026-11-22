FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY app.py schema.py train.py ./
COPY data/ data/
RUN python train.py
USER 10001
EXPOSE 8080
CMD ["sh", "-c", "waitress-serve --listen=0.0.0.0:${PORT:-8080} app:app"]
