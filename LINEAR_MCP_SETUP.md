# Настройка Linear MCP для Cursor

## Обзор

Linear MCP (Model Context Protocol) позволяет интегрировать Linear с Cursor IDE для автоматизации управления задачами и проектами через AI-ассистента.

## Текущий статус

✅ **Linear MCP настроен в конфигурации** (`C:\Users\renat\.cursor\mcp.json`)

Текущая конфигурация:
```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/mcp"]
    }
  }
}
```

❌ **Ошибка авторизации:** `InvalidGrantError: Invalid PKCE code_verifier`

**Проблема:** OAuth авторизация началась, но процесс обмена кода авторизации завершился с ошибкой PKCE.

**Решения:**
1. Очистить кэш npm и перезапустить авторизацию
2. Использовать альтернативный URL (`/sse` вместо `/mcp`)
3. Очистить сохраненные токены авторизации

## Инструкция по настройке

### Текущая конфигурация

Linear MCP уже настроен с использованием официального сервера:
- **Сервер:** `mcp-remote` через npx
- **URL:** `https://mcp.linear.app/mcp`
- **Файл конфигурации:** `C:\Users\renat\.cursor\mcp.json`

### Альтернативный вариант конфигурации

Если текущая конфигурация не работает, попробуйте использовать SSE endpoint:

```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/sse"]
    }
  }
}
```

### Шаг 2: Авторизация через настройки Cursor

1. Откройте Cursor Settings (Ctrl+, или File → Preferences → Settings)
2. Найдите раздел "MCP Servers" или "Model Context Protocol"
3. Найдите сервер "linear" в списке
4. Нажмите кнопку "Login", "Authorize" или "Connect"
5. Должен открыться браузер для OAuth авторизации в Linear
6. Предоставьте необходимые разрешения

### Шаг 3: OAuth авторизация

1. При первом подключении Linear MCP запустится OAuth-процесс
2. Авторизуйтесь в Linear через браузер
3. Предоставьте необходимые разрешения для доступа к вашей рабочей области

### Шаг 4: Проверка подключения

После настройки вы сможете:
- Создавать задачи в Linear через команды AI
- Обновлять статусы задач
- Управлять проектами и командами
- Получать информацию о задачах

## Требования

- **Linear аккаунт** с доступом к рабочей области KYA
- **Cursor IDE** с поддержкой MCP
- **Подписка Linear** (может потребоваться Pro план для некоторых функций)

## Полезные ссылки

- Linear команда: https://linear.app/kyamovvm/team/KYA/active
- Linear документация: https://linear.app/docs/default-team-pages#active
- MCP Bundles: https://www.mcpbundles.com/bundles/linear
- System Prompt: https://systemprompt.io/documentation/modules/linear

## После настройки

После успешной настройки Linear MCP вы сможете использовать команды типа:
- "Создай задачу в Linear для..."
- "Покажи все задачи в статусе In Progress"
- "Обнови статус задачи..."
- "Создай план проекта в Linear"

## Устранение неполадок

### Ошибка: `InvalidGrantError: Invalid PKCE code_verifier`

Эта ошибка возникает при проблемах с OAuth авторизацией. Решения:

1. **Очистите кэш npm и перезапустите авторизацию**
   ```powershell
   npm cache clean --force
   ```
   - Перезапустите Cursor
   - Попробуйте авторизоваться снова через Settings → MCP Servers → linear → Login

2. **Используйте SSE endpoint вместо MCP**
   - Измените URL в `mcp.json`:
     ```json
     "args": ["-y", "mcp-remote", "https://mcp.linear.app/sse"]
     ```
   - Перезапустите Cursor

3. **Очистите сохраненные токены**
   - Закройте Cursor
   - Удалите папку с кэшем авторизации (если есть)
   - Перезапустите Cursor и попробуйте авторизоваться заново

4. **Проверьте логи MCP**
   - Откройте Output панель (`Ctrl+Shift+U`)
   - Выберите "MCP Logs" в выпадающем списке
   - Проверьте детали ошибки

### Общие проблемы

Если MCP не работает (ресурсы не найдены):

1. **Перезапустите Cursor**
   - Полностью закройте Cursor
   - Запустите заново
   - MCP серверы загружаются при старте

2. **Проверьте авторизацию через настройки Cursor**
   - Откройте Settings → MCP Servers
   - Найдите сервер "linear"
   - Проверьте статус подключения
   - Если статус "Disconnected" или "Not Authorized", нажмите "Login"/"Authorize"
   - Проверьте логи Cursor на наличие ошибок авторизации

3. **Проверьте конфигурацию**
   - Убедитесь, что файл `C:\Users\renat\.cursor\mcp.json` корректен
   - Проверьте синтаксис JSON (нет лишних запятых, правильные кавычки)

4. **Проверьте доступность сервера**
   - Убедитесь, что `npx` доступен в PATH
   - Проверьте интернет-соединение
   - Попробуйте выполнить вручную: `npx -y mcp-remote https://mcp.linear.app/mcp`

5. **Альтернативные варианты**
   - Если текущий сервер не работает, можно попробовать другие варианты:
     - MCP Bundles: https://www.mcpbundles.com/bundles/linear
     - System Prompt: https://systemprompt.io/documentation/modules/linear

6. **Проверка версии Cursor**
   - Убедитесь, что используете последнюю версию Cursor
   - В старых версиях были проблемы с загрузкой `mcp.json`

