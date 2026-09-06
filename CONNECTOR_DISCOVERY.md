# Widen (Acquia DAM) Connector — Discovery

**Vendor:** Widen (Acquia DAM) (https://widen.com)  
**API Base URL:** `https://api.widencollective.com/v2`  
**Authentication:** Personal Access Token (Authorization: Bearer <token>)

## Архитектура API
- **Ключевые сущности:** цифровые ассеты (/assets), категории каталога (/categories), коллекции (/collections), мета-поля (/metadata)
- **Формат обмена данными:** JSON / HTTPS REST.
- **Обработка ошибок:** Стандартные HTTP-коды (400, 401, 403, 404, 429, 500) с типизацией ответа.
- **Тестовая точка проверки подключения:** `GET /v2/assets`.
