# Antispam ML API

Обучение, параметры и оценка качества приведены в основном ноутбуке Google Colab.

## Локальный запуск (вне Colab)
```
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Docker (в среде с установленным Docker)
```
docker build -t antispam-api .
docker run --rm -p 8000:8000 antispam-api
```

## Пример запроса
```
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"text":"Claim your prize now!"}'
```

Документация Swagger: http://localhost:8000/docs

Реальный публичный хостинг настраивается отдельно; сервис не предназначен для прямого подключения к личному почтовому ящику без дополнительной защиты.
