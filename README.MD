# Пустой проект на Django

### Описание:

- PDM менеджер зависимостей
- python==3.13.\*
- django>=5.1.2

### Установка:

```
brew install pdm
pdm init git@github.com:AlexandrBirukov/Empty-django-template-v1.git
```

### Запуск:

```
docker build -t empty .
docker run -it --rm -p 8000:8000 empty
```
