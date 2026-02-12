# KyaServer Monorepo

Главный репозиторий для управления несколькими проектами: основное приложение (Main), Docker контейнеры и документация.

## Паттерны

https://www.javadeploy.com/java-beans/module5/design-pattern-types.jsp

https://www.oreilly.com/library/view/java-enterprise-best/0596003846/ch02s01s04.html

https://www.oreilly.com/library/view/design-patterns-elements/0201633612/fm.html

## Cursor

https://forum.cursor.com/

## Obsidian

https://docs.obsidian.md/Plugins/User+interface/Status+bar

Cursor, Perplexity
https://linear.app/kyamovvm/project/kyaserver-monorepo-fd8e309de16d

## Структура

```text
kyaserver/
├── .cursor/              # Конфигурация и документация для Cursor
├── main-project/         # Git submodule → Main (основное приложение)
│   └── Japanese game/    # Игровой проект
├── wiki/                 # Git submodule → Main.wiki (документация)
├── docker-projects/      # Docker контейнеры и примеры
│   ├── bindmount-app/    # Приложение с bind mount
│   ├── getting-started-app/  # Учебное приложение
│   └── multi-container-app/  # Мульти-контейнерное приложение
├── tests/                # Тесты корневого уровня
├── compose.yaml          # Docker Compose конфигурация
├── Dockerfile            # Docker образ для основного приложения
└── package.json          # Зависимости корневого уровня
└── JP                    # Японский словарь и обучение
│   ├── agile/            # Agile система обучения (спринты, прогресс, трекинг)
│   │   ├── sprints/      # Спринты (текущий и архив)
│   │   ├── scripts/      # Скрипты автоматизации
│   │   ├── progress.md   # Общий прогресс
│   │   ├── kanban.md     # Доска задач
│   │   └── weekly-review.md # Еженедельные обзоры
│   └── Books/            # Книги для обучения на японском языке
└── EN                    # Английский словарь и обучение
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

## 📚 Документация

### Структура документации

Документация проекта состоит из нескольких частей:

1. **README.md** (этот файл) — быстрый старт и основные команды
2. **`.cursor/CURSOR.md`** — подробное руководство для работы с Cursor AI, архитектура проекта и лучшие практики
3. **`wiki/`** (Git submodule) — техническая документация в формате Markdown
4. **`CURSOR_EXTENSIONS_RECOMMENDATIONS.md`** — рекомендации по расширениям для Cursor IDE
5. **`JP/agile/`** — Agile система обучения японскому языку (спринты, прогресс, трекинг)

### Обучение японскому языку

Проект включает Agile систему для изучения японского языка с учётом ограниченного времени (40+ часов работы в неделю).

**Быстрый старт:**

```bash
cd JP/agile
# См. QUICK_START.md для подробностей
```

**Основные компоненты:**

- **Спринты** (2 недели) - планирование и отслеживание прогресса
- **Трекинг слов/кандзи** - JSON файлы для автоматизации
- **JS Game интеграция** - иммерсивная практика через визуальную новеллу
- **Скрипты** - автоматизация добавления слов/кандзи и обновления прогресса

**Цели:**

- 1500 слов (N5-N4 + SSW ресторанный словарь)
- 300 кандзи (N5-N4)
- **JFT-Basic 200+** (A2 уровень) - основной языковой тест (онлайн, проще JLPT)
- SSW Skills Test готовность (45 вопросов, 70 минут)

См. `JP/agile/README.md` и `JP/agile/QUICK_START.md` для подробностей.

### Ведение документации

#### Обновление README.md

- README.md содержит общую информацию о проекте
- Обновляйте при изменении структуры проекта, добавлении новых команд или зависимостей
- Используйте понятные заголовки и структурированные списки

#### Обновление `.cursor/CURSOR.md`

- Основной файл документации для Cursor AI
- Обновляйте при значительных изменениях в архитектуре проекта
- Включайте информацию о новых технологиях, паттернах и практиках
- Добавляйте примеры частых задач и их решения

#### Работа с wiki (Git submodule)

Wiki находится в отдельном репозитории (`Main.wiki`) и подключена как Git submodule.

**Создание новой статьи:**

```bash
cd wiki
# Создайте новый файл .md
# Используйте понятные имена в формате kebab-case (например: new-article.md)
# Добавьте ссылку в Home.md или соответствующем разделе
```

**Редактирование существующей статьи:**

```bash
cd wiki
# Отредактируйте нужный .md файл
git add .
git commit -m "Update documentation: описание изменений"
git push
cd ..
# Обновите ссылку на submodule в основном репозитории (если нужно)
git add wiki
git commit -m "Update wiki submodule"
git push
```

**Рекомендации по форматированию:**

- Используйте стандартный Markdown синтаксис
- Заголовки: `#` для H1, `##` для H2, `###` для H3
- Списки: `-` для маркированных, `1.` для нумерованных
- Код: `` `inline code` `` для фрагментов, тройные кавычки для блоков кода с указанием языка
- Внутренние ссылки: `[[filename.md]]` (если используется Obsidian) или `[текст](filename.md)`
- Изображения: храните в `wiki/` и ссылайтесь как `![alt](image.png)`

**Структура wiki:**

- `Home.md` — главная страница вики (точка входа)
- `1-overview.md`, `2-build.md`, и т.д. — нумерованные разделы документации
- Специализированные файлы: `idea-submodule.md`, `test-node.md`, `dev-containers.md` и т.д.

#### Обновление CURSOR_EXTENSIONS_RECOMMENDATIONS.md

- Обновляйте при изменении технологического стека проекта
- Добавляйте/удаляйте рекомендации по расширениям при добавлении новых технологий
- Включайте информацию о настройках и конфигурации расширений

### Лучшие практики

1. **Актуальность:** Регулярно обновляйте документацию при изменении проекта
2. **Ясность:** Пишите понятно, используйте примеры и код
3. **Структура:** Организуйте документацию логично, используйте оглавления
4. **Коммиты:** Делайте отдельные коммиты для документации с понятными сообщениями
5. **Согласованность:** Используйте единый стиль форматирования во всех файлах

### Полезные ссылки

- **Gitea репозиторий wiki:** http://192.168.0.104:3000/KyaMovVM/Main.wiki
- **Подробное руководство для Cursor:** `.cursor/CURSOR.md`

## Лицензия

none

## Ignore my old sister (First github)

https://github.com/VMYuki/web
https://gist.github.com/VMYuki/eb4bf230b47a6aba9022bebc8c160690
