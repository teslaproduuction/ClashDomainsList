# 🌐 ClashDomainsList

![GitHub last commit](https://img.shields.io/github/last-commit/teslaproduuction/ClashDomainsList)
![GitHub repo size](https://img.shields.io/github/repo-size/teslaproduuction/ClashDomainsList)
![GitHub stars](https://img.shields.io/github/stars/teslaproduuction/ClashDomainsList?style=social)

**[🇷🇺 Русский](README.md)** | **[us English](README_EN.md)**

Коллекция доменных списков для Clash и совместимых прокси-клиентов. Удобная категоризация доменов для гибкой маршрутизации трафика.

---

## 📋 Оглавление

- [Доступные категории](#-доступные-категории)
- [Быстрый старт](#-быстрый-старт)
- [Подробная настройка](#-подробная-настройка)
- [Примеры использования](#-примеры-использования)
- [Обновление списков](#-обновление-списков)
- [Структура репозитория](#-структура-репозитория)

---

## 🎯 Доступные категории

| Категория | Описание | Доменов | Ссылка |
|-----------|----------|---------|--------|
| <img src="ai.svg" width="200" alt="AI"> **AI** | AI сервисы (ChatGPT, Claude, Midjourney и др.) | ~50 | [ai.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/ai.txt) |
| <img src="discord.svg" width="200" alt="Discord"> **Discord** | Discord и связанные сервисы | ~3000 | [discord.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/discord.txt) |
| <img src="music.svg" width="200" alt="Music"> **Music** | Музыкальные стриминговые сервисы | ~200 | [music.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/music.txt) |
| <img src="porno.svg" width="200" alt="Porno"> **Porno** | Контент для взрослых | ~100 | [porno.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/porno.txt) |
| <img src="socials.svg" width="200" alt="Socials"> **Socials** | Социальные сети (Facebook, Instagram, Twitter и др.) | ~1000 | [socials.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/socials.txt) |
| <img src="tools.svg" width="200" alt="Tools"> **Tools** | Онлайн инструменты и сервисы | ~1000 | [tools.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/tools.txt) |
| <img src="telegram.svg" width="200" alt="Telegram"> **Telegram** | Telegram и связанные сервисы | ~50 | [telegram.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/telegram.txt) |
| <img src="torrent.svg" width="200" alt="Torrent"> **Torrent** | Торрент-трекеры и P2P сервисы | ~40 | [torrent.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/torrent.txt) |
| <img src="twitch.svg" width="200" alt="Twitch"> **Twitch** | Twitch и связанные стриминговые сервисы | ~14 | [twitch.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/twitch.txt) |
| <img src="whatsapp.svg" width="200" alt="WhatsApp"> **WhatsApp** | WhatsApp и связанные сервисы | ~30 | [whatsapp.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/whatsapp.txt) |
| <img src="youtube.svg" width="200" alt="YouTube"> **YouTube** | YouTube и связанные Google сервисы | ~8000 | [youtube.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/youtube.txt) |
| **Processes** | Правила по именам процессов (mihomo) | ~20 | [processes.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/processes.txt) |

---

## 🚀 Быстрый старт

### Шаг 1: Добавьте rule-providers в конфигурацию Clash

Откройте ваш конфигурационный файл Clash (обычно `config.yaml`) и добавьте секцию `rule-providers`:

```yaml
# Провайдеры правил для фильтрации трафика
rule-providers:
  ai:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/ai.txt"
    path: ./ruleset/ai.yaml
    interval: 86400

  porno:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/porno.txt"
    path: ./ruleset/porno.yaml
    interval: 86400

  discord:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/discord.txt"
    path: ./ruleset/discord.yaml
    interval: 86400

  youtube:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/youtube.txt"
    path: ./ruleset/youtube.yaml
    interval: 86400

  socials:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/socials.txt"
    path: ./ruleset/socials.yaml
    interval: 86400

  torrent:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/torrent.txt"
    path: ./ruleset/torrent.yaml
    interval: 86400

  tools:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/tools.txt"
    path: ./ruleset/tools.yaml
    interval: 86400

  music:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/music.txt"
    path: ./ruleset/music.yaml
    interval: 86400
```

### Шаг 2: Добавьте правила маршрутизации

Добавьте правила в секцию `rules`, чтобы определить, как обрабатывать трафик для каждой категории:

```yaml
rules:
  # AI сервисы через прокси
  - RULE-SET,ai,PROXY

  # Discord через прокси
  - RULE-SET,discord,PROXY

  # YouTube через прокси
  - RULE-SET,youtube,PROXY

  # Социальные сети через прокси
  - RULE-SET,socials,PROXY

  # Музыкальные сервисы через прокси
  - RULE-SET,music,PROXY

  # Торренты через прокси
  - RULE-SET,torrent,PROXY

  # Инструменты через прокси
  - RULE-SET,tools,PROXY

  # Блокировка контента для взрослых
  - RULE-SET,porno,REJECT

  # Остальной трафик по умолчанию
  - MATCH,DIRECT
```

### Шаг 3: Перезапустите Clash

После изменения конфигурации перезапустите Clash для применения новых правил.

---

## ⚙️ Подробная настройка

### Параметры rule-providers

| Параметр | Описание | Значение |
|----------|----------|----------|
| `type` | Тип провайдера | `http` - загрузка из интернета |
| `behavior` | Тип правил | `domain` - правила для доменов |
| `url` | URL списка доменов | Ссылка на raw файл в GitHub |
| `path` | Локальный путь кэша | Путь для сохранения загруженных правил |
| `interval` | Интервал обновления | `86400` = 24 часа (в секундах) |

### Действия для правил

| Действие | Описание | Пример использования |
|----------|----------|----------------------|
| `PROXY` | Направить через прокси-сервер | Тунелированное подключение |
| `DIRECT` | Прямое подключение без прокси | Локальные ресурсы |
| `REJECT` | Заблокировать соединение | Блокировка рекламы/нежелательного контента |

---

## 💡 Примеры использования

### Пример 1: Базовая настройка

```yaml
rule-providers:
  socials:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/socials.txt"
    path: ./ruleset/socials.yaml
    interval: 86400

rules:
  - RULE-SET,socials,PROXY
  - MATCH,DIRECT
```

### Пример 2: Селективная маршрутизация с группами прокси

```yaml
proxy-groups:
  - name: "AI Services"
    type: select
    proxies:
      - "US Server"
      - "EU Server"

  - name: "Streaming"
    type: select
    proxies:
      - "Fast Server"
      - "DIRECT"

rule-providers:
  ai:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/ai.txt"
    path: ./ruleset/ai.yaml
    interval: 86400

  youtube:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/youtube.txt"
    path: ./ruleset/youtube.yaml
    interval: 86400

rules:
  - RULE-SET,ai,AI Services
  - RULE-SET,youtube,Streaming
  - MATCH,DIRECT
```

### Пример 3: Родительский контроль

```yaml
rule-providers:
  porno:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/porno.txt"
    path: ./ruleset/porno.yaml
    interval: 86400

rules:
  - RULE-SET,porno,REJECT
  - MATCH,DIRECT
```

### Пример 4: Оптимизация для геймеров

```yaml
rule-providers:
  discord:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/discord.txt"
    path: ./ruleset/discord.yaml
    interval: 86400

  music:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/music.txt"
    path: ./ruleset/music.yaml
    interval: 86400

proxy-groups:
  - name: "Low Latency"
    type: url-test
    proxies:
      - "Gaming Server 1"
      - "Gaming Server 2"
    url: 'http://www.gstatic.com/generate_204'
    interval: 300

rules:
  - RULE-SET,discord,Low Latency
  - RULE-SET,music,PROXY
  - MATCH,DIRECT
```

---

## 🔧 Правила по процессам (mihomo / Clash Verge)

Файл `processes.txt` использует `behavior: classical` и содержит правила `PROCESS-NAME` / `PROCESS-NAME-REGEX` для маршрутизации по имени приложения.

> **Важно:** Конвертация в `.mrs` **не поддерживается** для classical behavior. Используйте `format: text` или `format: yaml`.

### Подключение (все процессы через один прокси)

```yaml
find-process-mode: always  # Обязательно для работы PROCESS-NAME

rule-providers:
  processes:
    type: http
    behavior: classical
    format: text
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/processes.txt"
    path: ./ruleset/processes.yaml
    interval: 86400

rules:
  - RULE-SET,processes,PROXY
  - MATCH,DIRECT
```

### Раздельная маршрутизация по категориям

Если нужны разные прокси-группы для разных приложений, добавьте правила напрямую в `rules`:

```yaml
find-process-mode: always

rules:
  # Discord
  - PROCESS-NAME-REGEX,(?i).*discord.*,PROXY Discord
  - PROCESS-NAME,Update.exe,PROXY Discord

  # AI
  - PROCESS-NAME-REGEX,(?i).*claude.*,PROXY AI
  - PROCESS-NAME-REGEX,(?i).*chatgpt.*,PROXY AI

  # YouTube
  - PROCESS-NAME-REGEX,(?i).*youtube.*,PROXY YouTube

  # Socials
  - PROCESS-NAME-REGEX,(?i).*twitter.*,PROXY Socials
  - PROCESS-NAME-REGEX,(?i).*telegram.*,PROXY Socials
  - PROCESS-NAME-REGEX,(?i).*instagram.*,PROXY Socials

  # Music
  - PROCESS-NAME-REGEX,(?i).*spotify.*,PROXY Music

  # Torrent
  - PROCESS-NAME-REGEX,(?i).*qbittorrent.*,PROXY Torrent
  - PROCESS-NAME-REGEX,(?i).*transmission.*,PROXY Torrent

  # Доменные правила
  - RULE-SET,youtube,PROXY YouTube
  - RULE-SET,discord,PROXY Discord
  - MATCH,DIRECT
```

### Платформы и имена процессов

| Платформа | Формат имени процесса | Пример |
|-----------|----------------------|--------|
| Windows | `Name.exe` | `Discord.exe`, `Spotify.exe` |
| macOS | `Name` | `Discord`, `Spotify` |
| Linux | `name` | `discord`, `spotify` |
| Android | `package.name` | `com.discord`, `com.spotify.music` |

> **Примечание:** На Linux/macOS может потребоваться запуск mihomo с правами `sudo` или capabilities `CAP_NET_ADMIN` + `CAP_SYS_PTRACE` для определения имён процессов.

---

## 🔄 Обновление списков

Списки доменов обновляются автоматически каждые 24 часа (по умолчанию) благодаря параметру `interval: 86400`.

### Изменение частоты обновления

```yaml
rule-providers:
  ai:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/ai.txt"
    path: ./ruleset/ai.yaml
    interval: 43200  # 12 часов
```

Рекомендуемые значения:
- `43200` - 12 часов (для часто обновляемых списков)
- `86400` - 24 часа (рекомендуется по умолчанию)
- `604800` - 7 дней (для стабильных списков)

### Принудительное обновление

Для принудительного обновления удалите кэш:
```bash
rm -rf ./ruleset/*.yaml
```

После перезапуска Clash загрузит свежие версии списков.

---

## 📁 Структура репозитория

```
ClashDomainsList/
├── README.md          # Этот файл
├── ai.txt             # AI сервисы
├── ai.svg             # Иконка категории
├── discord.txt        # Discord
├── discord.svg
├── music.txt          # Музыкальные сервисы
├── music.svg
├── porno.txt          # Контент для взрослых
├── porno.svg
├── socials.txt        # Социальные сети
├── socials.svg
├── tools.txt          # Онлайн инструменты
├── tools.svg
├── torrent.txt        # Торрент-трекеры
├── torrent.svg
├── youtube.txt        # YouTube
├── youtube.svg
└── processes.txt      # Правила по процессам (classical)
```

### Формат файлов

Все `.txt` файлы используют формат Clash YAML:

```yaml
payload:
  - '+.example.com'      # Домен и все поддомены
  - 'www.example.com'    # Только конкретный домен
  - 'example.com'        # Точное совпадение
```

---

## 🤝 Вклад в проект

Нашли недостающий домен или ошибку? Создайте Pull Request или Issue!

### Правила добавления доменов:

1. Домены должны соответствовать категории
2. Проверьте, что домен еще не добавлен
3. Используйте правильный формат:
   - `'+.domain.com'` - для домена и всех поддоменов
   - `'domain.com'` - для точного совпадения

---

## 📝 Лицензия

Этот проект распространяется свободно для личного и коммерческого использования.

---

## ⭐ Поддержка проекта

Если этот проект оказался полезным, поставьте ⭐ на GitHub!

---

## 📮 Контакты

- GitHub Issues: [teslaproduuction/ClashDomainsList/issues](https://github.com/teslaproduuction/ClashDomainsList/issues)
- Pull Requests: [teslaproduuction/ClashDomainsList/pulls](https://github.com/teslaproduuction/ClashDomainsList/pulls)

---

<div align="center">

**Сделано с ❤️ для сообщества Clash**

[⬆ Наверх](#-clashdomainslist)

</div>
