# 🔍 follower-lens

> Instantly peek at any public Instagram profile's **followers**, **following**, and **post count** — no login, no API key required.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/Frontend-HTML%2FJS-E34F26?style=flat-square&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ What It Does

**follower-lens** is a lightweight tool that scrapes Instagram's public HTML page to extract profile statistics. It consists of:

- 🐍 **`app.py`** — A Flask backend that fetches and parses Instagram's public profile page
- 🌐 **`index.html`** — A sleek, dark-themed frontend (InstaScope UI) to interact with the API

Simply paste a profile URL, username, or `@handle` and get the stats back in seconds.

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install flask flask-cors requests
```

### Run the backend

```bash
python app.py
```

The server starts at `http://localhost:5000`.

### Open the frontend

Just open `index.html` in your browser. Make sure `app.py` is running first.

---

## 🛠️ How It Works

1. You submit a username or Instagram URL
2. The Flask server requests Instagram's **public profile page** (no login, no API)
3. It parses the `<meta>` tags in the HTML response to extract follower/following/post data
4. Results are returned as JSON and displayed in the UI

---

## ⚠️ Known Limitations

> **Read this before using — the data may not always be perfectly accurate.**

### 1. 📦 Cached / Stale HTML from Instagram

This is the **biggest limitation** of this tool.

Instagram does **not** update a profile's public HTML page in real time. When you follow or unfollow someone, Instagram's servers may take anywhere from **a few minutes to several hours** to reflect the new count in the page's raw HTML. This means:

- If you just followed someone, their **follower count shown here may still be the old value**
- If someone just unfollowed you, the decrease might not show up immediately
- The numbers you see are essentially **Instagram's cached snapshot**, not a live feed

> **Bottom line:** The stats are accurate to within a reasonable window, but do not treat them as real-time. Think of them as a *recently-cached* value.

---

### 2. 🔒 Private Profiles Don't Work

This tool only works on **public Instagram profiles**. If the account is set to private, Instagram's HTML won't contain any stat data and the tool will return an error.

---

### 3. 🤖 Instagram Anti-Scraping Measures

Instagram actively tries to detect and block automated requests. If you make too many requests in a short period, Instagram may:

- Return a `429 Too Many Requests` response
- Redirect to a login page
- Temporarily block your IP

Use this tool **responsibly and sparingly**.

---

### 4. 🌐 No Official API — Subject to Breaking

This tool works by reading Instagram's **raw HTML**, not an official API. Instagram can change their page structure at any time without notice, which could break the parser. If the tool suddenly stops returning data, the HTML format likely changed.

---

### 5. 🖥️ Requires Local Server

The frontend (`index.html`) calls `localhost:5000`. You **must** have `app.py` running on your machine for it to work. It is not a hosted web service.

---

## 📁 Project Structure

```
follower-lens/
├── app.py        # Flask backend — scraping & parsing logic
├── index.html    # Frontend UI (InstaScope)
└── README.md
```

---

## 📡 API Reference

### `POST /quick_scrape`

**Request body:**
```json
{ "url": "instagram.com/cristiano" }
```

**Response:**
```json
{
  "username": "cristiano",
  "full_name": "Cristiano Ronaldo",
  "followers": 636000000,
  "following": 567,
  "posts": 3900,
  "profile_url": "https://www.instagram.com/cristiano/"
}
```

Accepts full URLs, `@handles`, or plain usernames.

---

## ⚖️ Disclaimer

This project is intended for **educational and personal use only**. It does not use Instagram's official API and may violate Instagram's Terms of Service if misused. The author is not responsible for any misuse or consequences arising from the use of this tool. Use at your own risk.

---

## 📄 License

MIT © [Xyrus72](https://github.com/Xyrus72)
