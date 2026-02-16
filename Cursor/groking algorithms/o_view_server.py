#!/usr/bin/env python3
"""
Простой HTTP-сервер для визуализации O(n) в браузере.
Рисование квадратов через Canvas (JS) + CSS.
И другого кода
"""

import os
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


class OViewHandler(SimpleHTTPRequestHandler):
    """Обработчик: отдаёт o_view.html как главную страницу."""

    def __init__(self, *args, directory=None, **kwargs):
        self.directory = directory or str(Path(__file__).parent)
        super().__init__(*args, directory=self.directory, **kwargs)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.path = "/o_view.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")


def main():
    port = 8888
    directory = Path(__file__).parent
    os.chdir(directory)

    server = HTTPServer(("", port), lambda *a, **k: OViewHandler(*a, directory=str(directory), **k))
    url = f"http://127.0.0.1:{port}/"

    print(f"Сервер запущен: {url}")
    print("O-большое: визуализация рисования квадратов (O(n))")
    print("Нажмите Ctrl+C для остановки")
    print()

    try:
        webbrowser.open(url)
    except Exception:
        print(f"Откройте в браузере: {url}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен")


if __name__ == "__main__":
    main()
