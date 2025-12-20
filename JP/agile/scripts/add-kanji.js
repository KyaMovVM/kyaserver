#!/usr/bin/env node
/**
 * Скрипт для добавления нового кандзи в трекер
 * Использование: node add-kanji.js "漢字" "чтения" "значение" [--level N5|N4]
 */

const fs = require('fs');
const path = require('path');

const KANJI_TRACKER = path.join(__dirname, '../kanji-tracker.json');

const args = process.argv.slice(2);
if (args.length < 3) {
  console.log('Использование: node add-kanji.js "漢字" "он-ёми,кун-ёми" "значение" [--level N5|N4]');
  process.exit(1);
}

const kanji = args[0];
const readings = args[1];
const meaning = args[2];
const level = args.includes('--level') 
  ? args[args.indexOf('--level') + 1] || 'N5'
  : 'N5';

// Читаем трекер
const tracker = JSON.parse(fs.readFileSync(KANJI_TRACKER, 'utf8'));

// Добавляем кандзи
const newKanji = {
  id: Date.now(),
  kanji: kanji,
  readings: readings.split(',').map(r => r.trim()),
  meaning: meaning,
  level: level,
  status: 'learning',
  added_date: new Date().toISOString().split('T')[0],
  last_reviewed: null,
  review_count: 0,
  stroke_count: null // можно добавить позже
};

tracker.kanji.push(newKanji);
tracker.statistics.total_learned = tracker.kanji.length;
tracker.statistics.by_level[level] = (tracker.statistics.by_level[level] || 0) + 1;
tracker.statistics.by_status.learning += 1;
tracker.metadata.last_updated = new Date().toISOString();

// Сохраняем
fs.writeFileSync(KANJI_TRACKER, JSON.stringify(tracker, null, 2), 'utf8');

console.log(`✅ Кандзи добавлен: ${kanji} (${readings}) - ${meaning} [${level}]`);
console.log(`   Всего кандзи: ${tracker.statistics.total_learned} / ${tracker.metadata.total_goal}`);

