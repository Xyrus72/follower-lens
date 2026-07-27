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



### . 🖥️ Requires Local Server

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


---

## 📄 License

MIT © [Xyrus72](https://github.com/Xyrus72)
