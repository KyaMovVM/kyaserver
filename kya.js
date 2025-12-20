#!/usr/bin/env node
// Простой HTTP-сервер, показывающий рекурсивный список файлов проекта.
const http = require('http');
const fs = require('fs').promises;
const fsSync = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3100;
const ROOT = process.cwd();

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":"&#39;"})[c]);
}

async function walk(dir) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  let results = [];
  for (const ent of entries) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      const sub = await walk(full);
      results.push(...sub);
    } else {
      results.push(path.relative(ROOT, full).replace(/\\/g, '/'));
    }
  }
  return results;
}

const server = http.createServer(async (req, res) => {
  try {
    if (req.url === '/' || req.url === '/index.html') {
      const files = await walk(ROOT);
      const items = files.map(f => `<li><a href="/raw/${encodeURIComponent(f)}">${escapeHtml(f)}</a></li>`).join('\n');
      const html = `<!doctype html><meta charset="utf-8"><title>Files</title><h1>Project files</h1><ul>${items}</ul>`;
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(html);
      return;
    }

    if (req.url.startsWith('/raw/')) {
      const rel = decodeURIComponent(req.url.slice('/raw/'.length));
      const full = path.join(ROOT, rel);
      if (!full.startsWith(ROOT)) {
        res.writeHead(400, { 'Content-Type': 'text/plain' });
        res.end('Invalid path');
        return;
      }
      if (!fsSync.existsSync(full)) {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not found');
        return;
      }
      const stat = fsSync.statSync(full);
      if (stat.isDirectory()) {
        res.writeHead(400, { 'Content-Type': 'text/plain' });
        res.end('Is a directory');
        return;
      }
      const stream = fsSync.createReadStream(full);
      res.writeHead(200, { 'Content-Type': 'application/octet-stream' });
      stream.pipe(res);
      return;
    }

    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not found');
  } catch (err) {
    res.writeHead(500, { 'Content-Type': 'text/plain' });
    res.end('Error: ' + (err && err.message ? err.message : String(err)));
  }
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`File index server running at http://0.0.0.0:${PORT}/`);
});

