<div align="center">
  <img src="https://github.com/user-attachments/assets/90fa61da-3b5f-4f7b-9b37-468fbfff9d0c" alt="Description"/>
</div>


## Описание

Данный проект является веб-приложением для анализа действий людей по видеопоследовательности.

Автор: Мещеряков Сергей

Стек (планируемый):
1. Backend - Django + FastAPI;
2. Frontend - React JS (верьте мне);
3. Devops - Docker + Docker Compose;
4. ML - Pytorch + OpenCV + Ultralytics (YOLO) + ByteTrack/Deep Sort + I3D (или что-то такое)

MVP:
1. Full backend;
2. Working (not beautiful) frontend;
3. Docker Compose;
4. Models.

Планы:
1. Добавить распознавание по потоковому видео;
2. Kubernetes;
3. Redis/RabbitMQ/Kafka;
4. Выбор разных моделей для детекции/трекинга.

## Документация

### Модели

Для описания orm моделей используются встроенные в Django инструменты.

1. Модель пользователя - наследуется от Abstractuser. Поддерживает вход по username и password.
2. Модель видео - содержит поля с путями к файлам - изначального и обработанного.
3. 

### Методы api


