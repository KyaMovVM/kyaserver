#!/bin/bash
# Скрипт для push всех подмодулей и основного репозитория
# Выполните в интерактивном терминале (авторизация нужна)

set -e

cd "$(dirname "$0")"

echo "=== Push KyaMovVM.github.io ==="
cd KyaMovVM.github.io && git push && cd ..

echo "=== Push main-project ==="
cd main-project && git push && cd ..

echo "=== Push wiki ==="
cd wiki && git push && cd ..

echo "=== Push kyaserver (main) ==="
git push

echo "=== Готово! ==="
