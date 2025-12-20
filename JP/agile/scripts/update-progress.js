#!/usr/bin/env node
/**
 * Скрипт для обновления прогресса обучения японскому
 * Использование: node update-progress.js [--words X] [--kanji Y] [--genki Z] [--minna W]
 */

const fs = require('fs');
const path = require('path');

const PROGRESS_FILE = path.join(__dirname, '../progress.md');
const WORDS_TRACKER = path.join(__dirname, '../words-tracker.json');
const KANJI_TRACKER = path.join(__dirname, '../kanji-tracker.json');

// Парсинг аргументов командной строки
const args = process.argv.slice(2);
const options = {};
args.forEach((arg, index) => {
  if (arg.startsWith('--')) {
    const key = arg.slice(2);
    const value = args[index + 1];
    if (value && !value.startsWith('--')) {
      options[key] = parseInt(value, 10);
    }
  }
});

function updateProgress() {
  // Читаем текущий прогресс
  let progressContent = fs.readFileSync(PROGRESS_FILE, 'utf8');
  
  // Обновляем слова
  if (options.words !== undefined) {
    const wordsMatch = progressContent.match(/Текущее:\s*(\d+)\s*\/\s*1500/);
    if (wordsMatch) {
      const current = parseInt(wordsMatch[1], 10);
      const newValue = current + options.words;
      progressContent = progressContent.replace(
        /Текущее:\s*\d+\s*\/\s*1500/,
        `Текущее: ${newValue} / 1500`
      );
      progressContent = progressContent.replace(
        /\((\d+)%\)/,
        `(${Math.round((newValue / 1500) * 100)}%)`
      );
    }
  }
  
  // Обновляем кандзи
  if (options.kanji !== undefined) {
    const kanjiMatch = progressContent.match(/Текущее:\s*(\d+)\s*\/\s*300/);
    if (kanjiMatch) {
      const current = parseInt(kanjiMatch[1], 10);
      const newValue = current + options.kanji;
      progressContent = progressContent.replace(
        /Текущее:\s*\d+\s*\/\s*300/,
        `Текущее: ${newValue} / 300`
      );
    }
  }
  
  // Обновляем дату
  const now = new Date().toLocaleDateString('ru-RU');
  progressContent = progressContent.replace(
    /\*\*Последнее обновление:\*\*.*/,
    `**Последнее обновление:** ${now}`
  );
  
  // Сохраняем
  fs.writeFileSync(PROGRESS_FILE, progressContent, 'utf8');
  
  console.log('✅ Прогресс обновлён!');
  if (options.words) console.log(`   Слова: +${options.words}`);
  if (options.kanji) console.log(`   Кандзи: +${options.kanji}`);
}

// Запуск
if (Object.keys(options).length > 0) {
  updateProgress();
} else {
  console.log('Использование:');
  console.log('  node update-progress.js --words 10 --kanji 5');
  console.log('  node update-progress.js --genki 1');
  console.log('  node update-progress.js --minna 1');
}

