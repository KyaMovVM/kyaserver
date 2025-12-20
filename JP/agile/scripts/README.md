# Скрипты для автоматизации

## 📝 Доступные скрипты

### `add-word.js`
Добавляет новое слово в трекер.

**Использование:**
```bash
node add-word.js "слово" "чтение" "значение" [--level N5|N4|SSW]
```

**Примеры:**
```bash
node add-word.js "私" "watashi" "я" --level N5
node add-word.js "本" "hon" "книга" --level N5
node add-word.js "レストラン" "resutoran" "ресторан" --level SSW
```

### `add-kanji.js`
Добавляет новый кандзи в трекер.

**Использование:**
```bash
node add-kanji.js "漢字" "он-ёми,кун-ёми" "значение" [--level N5|N4]
```

**Примеры:**
```bash
node add-kanji.js "私" "watashi,shi" "я" --level N5
node add-kanji.js "本" "hon,moto" "книга,основа" --level N5
```

### `update-progress.js`
Обновляет общий прогресс в `progress.md`.

**Использование:**
```bash
node update-progress.js [--words X] [--kanji Y] [--genki Z] [--minna W]
```

**Примеры:**
```bash
# Добавить 10 слов и 5 кандзи
node update-progress.js --words 10 --kanji 5

# Завершить урок Genki
node update-progress.js --genki 1

# Завершить урок Minna
node update-progress.js --minna 1
```

## 🔧 Настройка (Windows)

В Windows PowerShell можно создать алиасы:

```powershell
# Добавить в профиль PowerShell ($PROFILE)
function Add-JPWord {
    param($word, $reading, $meaning, $level = "N5")
    node "$PSScriptRoot\add-word.js" $word $reading $meaning --level $level
}

function Add-JPKanji {
    param($kanji, $readings, $meaning, $level = "N5")
    node "$PSScriptRoot\add-kanji.js" $kanji $readings $meaning --level $level
}

function Update-JPProgress {
    param($words = 0, $kanji = 0, $genki = 0, $minna = 0)
    $args = @()
    if ($words -gt 0) { $args += "--words"; $args += $words }
    if ($kanji -gt 0) { $args += "--kanji"; $args += $kanji }
    if ($genki -gt 0) { $args += "--genki"; $args += $genki }
    if ($minna -gt 0) { $args += "--minna"; $args += $minna }
    node "$PSScriptRoot\update-progress.js" $args
}
```

Использование:
```powershell
Add-JPWord "私" "watashi" "я" "N5"
Add-JPKanji "本" "hon,moto" "книга" "N5"
Update-JPProgress -words 10 -kanji 5
```

## 📊 Формат данных

### words-tracker.json
```json
{
  "words": [
    {
      "id": 1234567890,
      "word": "私",
      "reading": "watashi",
      "meaning": "я",
      "level": "N5",
      "status": "learning",
      "added_date": "2025-12-20",
      "last_reviewed": null,
      "review_count": 0
    }
  ]
}
```

### kanji-tracker.json
```json
{
  "kanji": [
    {
      "id": 1234567890,
      "kanji": "本",
      "readings": ["hon", "moto"],
      "meaning": "книга, основа",
      "level": "N5",
      "status": "learning",
      "added_date": "2025-12-20",
      "last_reviewed": null,
      "review_count": 0,
      "stroke_count": null
    }
  ]
}
```

## 🚀 Автоматизация

Можно настроить автоматический запуск скриптов:

### Windows Task Scheduler
1. Создать батник `daily-update.bat`:
```batch
@echo off
cd /d "C:\kyaserver\JP\agile\scripts"
node update-progress.js --words 5
```

2. Настроить Task Scheduler для ежедневного запуска

### Cron (Linux/Mac)
```bash
# Ежедневно в 20:00
0 20 * * * cd /path/to/kyaserver/JP/agile/scripts && node update-progress.js --words 5
```

