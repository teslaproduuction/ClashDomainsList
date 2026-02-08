# 🌐 ClashDomainsList

![GitHub last commit](https://img.shields.io/github/last-commit/teslaproduuction/ClashDomainsList)
![GitHub repo size](https://img.shields.io/github/repo-size/teslaproduuction/ClashDomainsList)
![GitHub stars](https://img.shields.io/github/stars/teslaproduuction/ClashDomainsList?style=social)

**[🇷🇺 Русский](README.md)** | **[us English](README_EN.md)**

A collection of domain lists for Clash and compatible proxy clients. Convenient domain categorization for flexible traffic routing.

---

## 📋 Table of Contents

- [Available Categories](#-available-categories)
- [Quick Start](#-quick-start)
- [Detailed Configuration](#-detailed-configuration)
- [Usage Examples](#-usage-examples)
- [Updating Lists](#-updating-lists)
- [Repository Structure](#-repository-structure)

---

## 🎯 Available Categories

| Category | Description | Domains | Link |
|----------|-------------|---------|------|
| <img src="ai.svg" width="200" alt="AI"> **AI** | AI services (ChatGPT, Claude, Midjourney, etc.) | ~50 | [ai.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/ai.txt) |
| <img src="discord.svg" width="200" alt="Discord"> **Discord** | Discord and related services | ~3000 | [discord.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/discord.txt) |
| <img src="music.svg" width="200" alt="Music"> **Music** | Music streaming services | ~200 | [music.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/music.txt) |
| <img src="porno.svg" width="200" alt="Porno"> **Porno** | Adult content | ~100 | [porno.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/porno.txt) |
| <img src="socials.svg" width="200" alt="Socials"> **Socials** | Social networks (Facebook, Instagram, Twitter, etc.) | ~1000 | [socials.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/socials.txt) |
| <img src="tools.svg" width="200" alt="Tools"> **Tools** | Online tools and services | ~1000 | [tools.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/tools.txt) |
| <img src="torrent.svg" width="200" alt="Torrent"> **Torrent** | Torrent trackers and P2P services | ~40 | [torrent.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/torrent.txt) |
| <img src="youtube.svg" width="200" alt="YouTube"> **YouTube** | YouTube and related Google services | ~8000 | [youtube.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/youtube.txt) |
| **Processes** | Process name rules (mihomo) | ~20 | [processes.txt](https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/processes.txt) |

---

## 🚀 Quick Start

### Step 1: Add rule-providers to Clash configuration

Open your Clash configuration file (usually `config.yaml`) and add the `rule-providers` section:

```yaml
# Rule providers for traffic filtering
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

### Step 2: Add routing rules

Add rules to the `rules` section to define how to handle traffic for each category:

```yaml
rules:
  # AI services through proxy
  - RULE-SET,ai,PROXY

  # Discord through proxy
  - RULE-SET,discord,PROXY

  # YouTube through proxy
  - RULE-SET,youtube,PROXY

  # Social networks through proxy
  - RULE-SET,socials,PROXY

  # Music services through proxy
  - RULE-SET,music,PROXY

  # Torrents through proxy
  - RULE-SET,torrent,PROXY

  # Tools through proxy
  - RULE-SET,tools,PROXY

  # Block adult content
  - RULE-SET,porno,REJECT

  # Default traffic routing
  - MATCH,DIRECT
```

### Step 3: Restart Clash

After modifying the configuration, restart Clash to apply the new rules.

---

## ⚙️ Detailed Configuration

### Rule-providers Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| `type` | Provider type | `http` - download from internet |
| `behavior` | Rule type | `domain` - domain rules |
| `url` | Domain list URL | Link to raw file on GitHub |
| `path` | Local cache path | Path to save downloaded rules |
| `interval` | Update interval | `86400` = 24 hours (in seconds) |

### Rule Actions

| Action | Description | Example Usage |
|--------|-------------|---------------|
| `PROXY` | Route through proxy server | Bypass blocking |
| `DIRECT` | Direct connection without proxy | Local resources |
| `REJECT` | Block connection | Block ads/unwanted content |

---

## 💡 Usage Examples

### Example 1: Basic Setup with Bypass

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

### Example 2: Selective Routing with Proxy Groups

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

### Example 3: Parental Control

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

### Example 4: Gaming Optimization

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

## 🔧 Process Rules (mihomo / Clash Verge)

The `processes.txt` file uses `behavior: classical` and contains `PROCESS-NAME` / `PROCESS-NAME-REGEX` rules for routing by application name.

> **Important:** `.mrs` conversion is **not supported** for classical behavior. Use `format: text` or `format: yaml`.

### Setup (all processes through one proxy)

```yaml
find-process-mode: always  # Required for PROCESS-NAME matching

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

### Per-category routing

For different proxy groups per application, add rules directly to `rules`:

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

  # Domain rules
  - RULE-SET,youtube,PROXY YouTube
  - RULE-SET,discord,PROXY Discord
  - MATCH,DIRECT
```

### Platforms and process names

| Platform | Process name format | Example |
|----------|-------------------|---------|
| Windows | `Name.exe` | `Discord.exe`, `Spotify.exe` |
| macOS | `Name` | `Discord`, `Spotify` |
| Linux | `name` | `discord`, `spotify` |
| Android | `package.name` | `com.discord`, `com.spotify.music` |

> **Note:** On Linux/macOS, mihomo may require `sudo` or capabilities `CAP_NET_ADMIN` + `CAP_SYS_PTRACE` to detect process names.

---

## 🔄 Updating Lists

Domain lists are automatically updated every 24 hours (by default) thanks to the `interval: 86400` parameter.

### Changing Update Frequency

```yaml
rule-providers:
  ai:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/teslaproduuction/ClashDomainsList/main/ai.txt"
    path: ./ruleset/ai.yaml
    interval: 43200  # 12 hours
```

Recommended values:
- `43200` - 12 hours (for frequently updated lists)
- `86400` - 24 hours (recommended default)
- `604800` - 7 days (for stable lists)

### Force Update

To force an update, delete the cache:
```bash
rm -rf ./ruleset/*.yaml
```

After restarting Clash, it will download fresh versions of the lists.

---

## 📁 Repository Structure

```
ClashDomainsList/
├── README.md          # Russian version
├── README_EN.md       # This file (English version)
├── ai.txt             # AI services
├── ai.svg             # Category icon
├── discord.txt        # Discord
├── discord.svg
├── music.txt          # Music services
├── music.svg
├── porno.txt          # Adult content
├── porno.svg
├── socials.txt        # Social networks
├── socials.svg
├── tools.txt          # Online tools
├── tools.svg
├── torrent.txt        # Torrent trackers
├── torrent.svg
├── youtube.txt        # YouTube
├── youtube.svg
└── processes.txt      # Process rules (classical behavior)
```

### File Format

All `.txt` files use Clash YAML format:

```yaml
payload:
  - '+.example.com'      # Domain and all subdomains
  - 'www.example.com'    # Specific domain only
  - 'example.com'        # Exact match
```

---

## 🤝 Contributing

Found a missing domain or error? Create a Pull Request or Issue!

### Domain Addition Rules:

1. Domains must match the category
2. Check that the domain hasn't been added yet
3. Use the correct format:
   - `'+.domain.com'` - for domain and all subdomains
   - `'domain.com'` - for exact match

---

## 📝 License

This project is distributed freely for personal and commercial use.

---

## ⭐ Support the Project

If this project was helpful, give it a ⭐ on GitHub!

---

## 📮 Contacts

- GitHub Issues: [teslaproduuction/ClashDomainsList/issues](https://github.com/teslaproduuction/ClashDomainsList/issues)
- Pull Requests: [teslaproduuction/ClashDomainsList/pulls](https://github.com/teslaproduuction/ClashDomainsList/pulls)

---

<div align="center">

**Made with ❤️ for the Clash community**

[⬆ Back to Top](#-clashdomainslist)

</div>

