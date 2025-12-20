#!/usr/bin/env node
/**
 * Скрипт для добавления нового слова в трекер
 * Использование: node add-word.js "слово" "чтение" "значение" [--level N5|N4|SSW]
 */

const fs = require('fs');
const path = require('path');

const WORDS_TRACKER = path.join(__dirname, '../words-tracker.json');

const args = process.argv.slice(2);
if (args.length < 3) {
  console.log('Использование: node add-word.js "слово" "чтение" "значение" [--level N5|N4|SSW]');
  process.exit(1);
}

const word = args[0];
const reading = args[1];
const meaning = args[2];
const level = args.includes('--level') 
  ? args[args.indexOf('--level') + 1] || 'N5'
  : 'N5';

// Читаем трекер
const tracker = JSON.parse(fs.readFileSync(WORDS_TRACKER, 'utf8'));

// Добавляем слово
const newWord = {
  id: Date.now(),
  word: word,
  reading: reading,
  meaning: meaning,
  level: level,
  status: 'learning',
  added_date: new Date().toISOString().split('T')[0],
  last_reviewed: null,
  review_count: 0
};

tracker.words.push(newWord);
tracker.statistics.total_learned = tracker.words.length;
tracker.statistics.by_level[level] = (tracker.statistics.by_level[level] || 0) + 1;
tracker.statistics.by_status.learning += 1;
tracker.metadata.last_updated = new Date().toISOString();

// Сохраняем
fs.writeFileSync(WORDS_TRACKER, JSON.stringify(tracker, null, 2), 'utf8');

console.log(`✅ Слово добавлено: ${word} (${reading}) - ${meaning} [${level}]`);
console.log(`   Всего слов: ${tracker.statistics.total_learned} / ${tracker.metadata.total_goal}`);

