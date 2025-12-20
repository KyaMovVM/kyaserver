# KyaServer Monorepo

Главный репозиторий для управления несколькими проектами: основное приложение (Main), Docker контейнеры и документация.

## Структура

```
kyaserver/
├── main-project/          # Git submodule → Main (основное приложение)
├── wiki/                  # Git submodule → Main.wiki (документация)
├── docker-projects/       # Docker контейнеры
│   ├── bindmount-app/
│   ├── getting-started-app/
│   └── multi-container-app/
├── tests/                 # Тесты корневого уровня
│   └── __tests__/
├── compose.yaml           # Docker Compose для локального разворачивания
├── Dockerfile             # Docker образ для основного приложения
└── package.json           # Зависимости для корневых тестов и скриптов
```

## Быстрый старт

### 1. Клонирование с submodules

```bash
git clone http://192.168.0.104:3000/KyaMovVM/kyaserver.git
cd kyaserver
git submodule update --init --recursive
```

### 2. Установка зависимостей

**Корневые зависимости (для тестов):**
```bash
npm install
```

**Для каждого Docker проекта отдельно** (если нужно):
```bash
cd docker-projects/bindmount-app
npm install
```

**Для основного приложения (Main):**
```bash
cd main-project
# Смотрите README там
```

## Тестирование

```bash
npm test                    # Запустить корневые тесты
npm run test -- __tests__/novel.test.js  # Конкретный тест
```

## Развертывание

```bash
# Запустить все контейнеры
docker-compose up -d

# Запустить specific сервис
docker-compose up -d bindmount-app
```

## Git управление

### Обновление submodules

```bash
# Обновить все submodules
git submodule update --remote

# Обновить конкретный submodule
cd main-project
git pull origin main
cd ..
git add main-project
git commit -m "Update main-project"
```

### Добавление изменений

```bash
# Добавить изменения в этом репозитории
git add .
git commit -m "Description"
git push

# Изменения в submodule требуют отдельного push
cd main-project
git add .
git commit -m "Description"
git push
cd ..
```

## Репозитории на Gitea

- **Main:** http://192.168.0.104:3000/KyaMovVM/Main
- **Main.wiki:** http://192.168.0.104:3000/KyaMovVM/Main.wiki
- **Kyaserver:** http://192.168.0.104:3000/KyaMovVM/kyaserver

## Конфликты package.json

Каждый Docker проект имеет **собственный** `package.json` для своих зависимостей:
- Корневой `package.json` → только тесты и скрипты корневого уровня
- `docker-projects/*/package.json` → зависимости контейнеров
- `main-project/package.json` → зависимости основного приложения

Это предотвращает конфликты версий между проектами.

## Лицензия

ISC
