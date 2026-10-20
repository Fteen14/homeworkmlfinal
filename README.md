# Antispam ML API

Обучение, параметры и оценка качества приведены в основном ноутбуке Google Colab.

## Пример запроса
```
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"text":"Claim your prize now you won 1000000!"}'
```

Документация Swagger: http://localhost:8000/docs

Реальный публичный хостинг настраивается отдельно; сервис не предназначен для прямого подключения к личному почтовому ящику без дополнительной защиты.
