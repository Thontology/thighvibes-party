# ThighVibes Party

<div align="center">
  <a href="./README.md">English</a>
</div>

####

<div align="center">
  <a href="https://github.com/Thontology/thighvibes-party">GitHub</a> ·
  <a href="#quick-start">Quick Start</a>
</div>

---

## Introduction

### 🚀 **A 3D NSFW desktop companion — VaM on your desktop!**

* ✅ **Limitless intimacy:** A digital lover that supports live streaming, immersive roleplay, explicit Tavern cards, NSFW meme packs, and device integration (including interactive toys).

* ✅ **Always-on presence:** VRM desktop avatars stay with you 24/7, with persistent memory, sandboxing, and real-time control of your digital and physical setup.

* ✅ **Modular enhancements:** Extend capabilities seamlessly with RAG, browser automation, Home Assistant, Dify, MCP, A2A, ComfyUI, and more.

* ✅ **Developer friendly:** Exposes OpenAI-compatible APIs and MCP protocol support, making integration and secondary development straightforward.

* ✅ **Cross-platform ready:** Runs on Windows/macOS/Linux natively, supports Docker deployment, and offers web access.

---

## Why an NSFW Fork?

The original project, [Super-Agent-Party](https://github.com/heshengtao/super-agent-party), was designed as a **general-purpose 3D AI desktop companion**.
**ThighVibes Party** takes the same powerful foundation and adapts it specifically for **adult use cases**:

* 🔥 Explicit roleplay and adult Tavern cards
* 🔥 Integration with NSFW media (memes, packs, streams)
* 🔥 Device support (interactive toys and smart-home kink setups)
* 🔥 A sandboxed but open platform for erotic AI experimentation

This fork is built to be **playful, intimate, and uncensored**, while preserving all the modular extensibility of the parent project.

---

## Quick Start

### Windows Desktop Installation

👉 [Download latest release](https://github.com/Thontology/thighvibes-party/releases)

⭐ **Note:** Install for *current user only* to avoid requiring administrator privileges on startup.

### macOS Desktop Installation

👉 [Download latest release](https://github.com/Thontology/thighvibes-party/releases)

After installing, run the following to remove macOS quarantine restrictions:

```bash
sudo xattr -dr com.apple.quarantine /Applications/ThighVibes-Party.app
```

### Linux Desktop Installation

* `.AppImage` (portable, no install required)
* `.deb` (for Debian/Ubuntu-based systems)

👉 [Download latest release](https://github.com/Thontology/thighvibes-party/releases)

### Docker Deployment (Recommended)

```bash
docker pull thontology/thighvibes-party:latest
docker run -d -p 3456:3456 -v ./thighvibes-data:/app/data thontology/thighvibes-party:latest
```

* ⭐ **Note:** Replace `./thighvibes-data` with any local folder. All data stays local and never uploads elsewhere.

* Access at: [http://localhost:3456/](http://localhost:3456/)

### Source Deployment

```bash
git clone https://github.com/Thontology/thighvibes-party.git
cd thighvibes-party
uv sync
npm install
./start_with_dev.sh   # or start_with_dev.bat on Windows
```

---

## Screenshots & Features

* **Custom VRM avatars** — build your own companion.
* **Explicit Tavern cards** — run NSFW character personalities with persistent memory.
* **Device integration** — connect and control interactive toys.
* **Tool ecosystem** — integrate RAG, browser control, Home Assistant, Dify, ComfyUI, MCP, A2A.
* **Developer APIs** — OpenAI-compatible, real-time streaming support.

---

## Hardware Requirements

* CPU: 2+ cores
* RAM: 2GB+

**Because all models are optional, you may use local engines or external APIs. Even a 2-core/2GB server can run the Docker build.**

---

## Usage

* **Desktop:** Launch via desktop icon.
* **Web/Docker:** Visit [http://localhost:3456/](http://localhost:3456/).
* **API:** Fully OpenAI-compatible.

Example:

```python
from openai import OpenAI
client = OpenAI(api_key="secret", base_url="http://localhost:3456/v1")
res = client.chat.completions.create(
  model="thighvibes-model",
  messages=[{"role": "user", "content": "Tell me a fantasy..."}]
)
print(res.choices[0].message.content)
```

---

## Disclaimer

This project is **explicitly NSFW**.

* Intended for **adults only (18+)**.
* No guarantee of safety, accuracy, or fitness for any purpose.
* Use at your own risk.

---

## License

Dual-licensed:

1. **AGPLv3** by default.
2. Commercial licensing available on request for closed-source deployments.

---

## Support

⭐ Star the repo if you enjoy it!

<div align="center">
  <img src="doc/image/star.gif" width="400" alt="star"/>
</div>
