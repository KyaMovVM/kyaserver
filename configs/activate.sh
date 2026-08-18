#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Активация конфигураций ==="

# --- ZSH ---
echo ""
echo "[zsh] Настройка .zshrc..."
if [ -f "$HOME/.zshrc" ] && [ ! -L "$HOME/.zshrc" ]; then
    BACKUP="$HOME/.zshrc.backup.$(date +%Y%m%d%H%M%S)"
    echo "  Бэкап текущего .zshrc -> $BACKUP"
    cp "$HOME/.zshrc" "$BACKUP"
fi
ln -sfn "$SCRIPT_DIR/.zshrc" "$HOME/.zshrc"
echo "  Симлинк: ~/.zshrc -> $SCRIPT_DIR/.zshrc"

# --- NVIM ---
echo ""
echo "[nvim] Настройка nvim..."
NVIM_SRC="$SCRIPT_DIR/nvim"
NVIM_DST="$HOME/.config/nvim"
# Проверяем, есть ли реальный конфиг (не только README)
NVIM_FILES=$(find "$NVIM_SRC" -type f ! -name 'README.md' 2>/dev/null | head -1)
if [ -n "$NVIM_FILES" ]; then
    if [ -d "$NVIM_DST" ] && [ ! -L "$NVIM_DST" ]; then
        BACKUP="$NVIM_DST.backup.$(date +%Y%m%d%H%M%S)"
        echo "  Бэкап текущего nvim конфига -> $BACKUP"
        mv "$NVIM_DST" "$BACKUP"
    fi
    mkdir -p "$(dirname "$NVIM_DST")"
    ln -sfn "$NVIM_SRC" "$NVIM_DST"
    echo "  Симлинк: ~/.config/nvim -> $NVIM_SRC"
else
    echo "  Пропущено: конфиг nvim пока пуст (только README.md)"
fi

# --- KITTY ---
echo ""
echo "[kitty] Настройка kitty..."
KITTY_SRC="$SCRIPT_DIR/kitty/kitty.conf"
KITTY_DST="$HOME/.config/kitty/kitty.conf"
if [ -f "$KITTY_SRC" ]; then
    mkdir -p "$HOME/.config/kitty"
    if [ -f "$KITTY_DST" ] && [ ! -L "$KITTY_DST" ]; then
        BACKUP="$KITTY_DST.backup.$(date +%Y%m%d%H%M%S)"
        echo "  Бэкап текущего kitty.conf -> $BACKUP"
        cp "$KITTY_DST" "$BACKUP"
    fi
    ln -sfn "$KITTY_SRC" "$KITTY_DST"
    echo "  Симлинк: ~/.config/kitty/kitty.conf -> $KITTY_SRC"
fi

# --- GNOME TERMINAL ---
echo ""
echo "[gnome-terminal] Загрузка профиля..."
GNOME_CONF="$SCRIPT_DIR/gnome-terminal/gnome-terminal.dconf"
if [ -f "$GNOME_CONF" ] && command -v dconf >/dev/null 2>&1; then
    BACKUP="$SCRIPT_DIR/gnome-terminal/gnome-terminal.dconf.backup.$(date +%Y%m%d%H%M%S)"
    dconf dump /org/gnome/terminal/ > "$BACKUP"
    echo "  Бэкап текущих настроек -> $BACKUP"
    dconf load /org/gnome/terminal/ < "$GNOME_CONF"
    echo "  Настройки GNOME Terminal загружены из $GNOME_CONF"
else
    echo "  Пропущено: файл профиля не найден или команда dconf недоступна"
fi

# --- ЗАВИСИМОСТИ ---
echo ""
echo "[deps] Проверка Python-зависимостей..."
pip3 install --user --break-system-packages pynvim jupyter_client ipykernel 2>/dev/null && echo "  Python-пакеты установлены" || echo "  Ошибка установки Python-пакетов"
python3 -m ipykernel install --user --name python3 2>/dev/null && echo "  Jupyter kernel зарегистрирован" || echo "  Ошибка регистрации kernel"

echo ""
echo "[deps] Проверка luarock magick..."
if ! command -v magick >/dev/null 2>&1 && ! command -v convert >/dev/null 2>&1; then
    echo "  ImageMagick CLI не найден: установи 'sudo apt install imagemagick'"
fi
luarocks --local --lua-version 5.1 install magick 2>/dev/null && echo "  magick luarock установлен" || echo "  Ошибка установки magick (нужен libmagickwand-dev)"

echo ""
echo "=== Готово! ==="
echo "Запусти kitty и в нём nvim для полной поддержки картинок."
echo "Для применения zsh: exec zsh"
