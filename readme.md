<div align="center">
  <img src="https://github.com/user-attachments/assets/90fa61da-3b5f-4f7b-9b37-468fbfff9d0c" alt="Description"/>
</div>

## Описание

Данный проект является веб-приложением для анализа действий людей по видеопоследовательности.

Автор: Мещеряков Сергей

**Стек (планируемый):**
1. Backend - Django + FastAPI;
2. Frontend - React JS (верьте мне);
3. Devops - Docker + Docker Compose;
4. ML - Pytorch + OpenCV + Ultralytics (YOLO) + ByteTrack/Deep Sort + I3D (или что-то такое)

**MVP:**
1. Full backend;
2. Working (not beautiful) frontend;
3. Docker Compose;
4. Models.

**Планы:**
1. Добавить распознавание по потоковому видео;
2. Kubernetes;
3. Redis/RabbitMQ/Kafka;
4. Выбор разных моделей для детекции/трекинга.

## Структура

### Сервер

```
backend/
├── backend/
|   |─── api/
│        ├── serializers.py   # Сериализаторы
│        ├── urls.py          # Маршруты
│        └── views.py         # Методы
│   ├── settings.py      # Настройки (втф)
│   └── urls.py          # Маршруты
├── database/
│   └── models.py        # ORM-модели
├── manage.py
└── Dockerfile
```

### ML-сервис

```
ml_service/
├── app/
│   ├── app.py           # FastAPI приложение
│   ├── models.py        # Загрузка ML-моделей
│   ├── processing.py    # Логика обработки видео
├── requirements.txt
└── Dockerfile
```

## Документация

### Модели

Для описания orm моделей используются встроенные в Django инструменты.

1. **Модель пользователя** - наследуется от Abstractuser. Поддерживает вход по username и password.
2. **Модель видео** - содержит поля с путями к файлам - изначального и обработанного.
3. **Модель истории использования** - содержит поля для связи с другими объектами (User и VideoModel), статус обработки видео, названия моделей (для детекции, трекинга, анализа действий).

### Методы api

#### Сервер

1. **Register** - самописный метод для регистрации пользователя - users/register/. С помощью сериализатора создаётся объект и заполняются его поля.
2. **Login** - встроенный метод (TokenObtainPairView) для входа - users/login/.
3. **Refresh** - встроенный метод (TokenRefreshView) для обновления токена - users/refresh/.
4. **History** - самописный метод  для получения истории запросов на анализ видео - users/history/.
5. **Logout** - самописный метод для выхода из системы - users/logout/.
6. **Upload** - самописный метод для загрузки видео - upload/.
7. **Analyze** - самописный метод для анализа видео - analyze/.
8. **Result** - самописный метод для получения результата в виде видео/json - result/.

#### ML-сервис

1. **Process video** - самописный метод для обработки видео - process/.



