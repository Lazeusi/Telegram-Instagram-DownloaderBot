<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&section=header&text=Instagram%20Downloader%20Bot&fontSize=45&fontAlignY=35&animation=twinkling&fontColor=fff" />
</p>

<h3 align="center">🚀 Instagram media downloader Bot</h3>

<p align="center">
  <b>Built with:</b> Aiogram v3.22.0 • Async • MongoDB • FastAPI • yt-dlp
</p>

A modern Telegram bot to download **Instagram media** — posts, reels, and stories — with full admin control. Built for speed, stability, and easy management.

---

## 🛠️ Tech Stack
| Component | Description |
|------------|-------------|
| 🐍 Python 3.11+ | Core language |
| 🤖 Aiogram 3.22.0 | Telegram Bot framework |
| 🚀 FastAPI 0.119.1 | API |
| 🎞️ yt-dlp 2025.10.22 | Instagrm downloader |
| 🍃 MongoDB | Database |
| ⚡ Async / Await | Full async architecture |
| 🧰 Logging & Error Handling | Custom structured logging system |

### ✅ Media Download
- Download **videos and images** from Instagram.  
- Supports **public and private posts**.  
- Works in **groups** and **private chats**.  
- Files are stored in `media/instagram/YYYY-MM-DD/` for easy tracking or archival. (Optinial)

### 🔒 Admin & Owner Management
- If no admin exists, use: **/active_admin** to register yourself as **Owner**.  

- Only the **Owner** can add or remove admins using: `/panel`



- **Owner & admins** can also **ban/unban users** from the panel.  

### ⚙️ Smooth & Reliable
- Built with **Aiogram 3.x** for clean, modular bot handlers.  
- **FastAPI** API for downloading media independently.  
- **yt-dlp** with Chrome cookies support to prevent Instagram rate limits.  
- **Loguru** for detailed, professional logging.

---

## 🏗️ Setup

1. Clone the repository:

```bash
git clone <https://github.com/Lazeusi/Telegram-Instagram-Downloader.git>
cd <repo_name>
```
- Create a virtual environment and install dependencies:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```

- Create a .env file:
```.env
- BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
- API_URL=http://127.0.0.1:8000
```
- Start FastAPI (API) and Bot: *python main.py*

python -m src.bot
> 🔹 Note: Instagram downloads require internet access; a VPN may be necessary in restricted regions.

## 📌 How It Works
Send an Instagram link → the bot downloads and sends the media.

- Use `/active_admin` to become Owner if no admin exists.

- Use `/panel` to add/remove admins or ban/unban users.

- Works in group chats and private messages seamlessly.

## 🔧 Pro Tips

- VPN / Proxy: Required in `restricted` regions.

- Media storage: Files are organized by date for easy management.

- Login into instagram from firefox 

- Owner & Admin: Full control over user management and moderation.

## 🏅 Why This Bot
- Combines Aiogram + FastAPI + yt-dlp for a professional, production-ready bot that delivers:

- Complete admin management

- Safe, unlimited downloads

- Instant media delivery in groups & private chats

## ❤️ Support
- Star the repo ⭐, report issues, or contribute enhancements.


## 🧑‍💻 Author : **Shayan**

- Python Developer — Focused on Aiogram, FastAPI, and automation projects.
> | 🔗 GitHub: github.com/Lazeusi
> | 🐍 Telegram: @lazeusi

<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer"/> </p>
