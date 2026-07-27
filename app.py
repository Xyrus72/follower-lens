import re
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept":                  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language":         "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Mode":          "navigate",
    "Sec-Fetch-Site":          "none",
    "Sec-Fetch-Dest":          "document",
}


def parse_num(s: str) -> int:
    """'1.2M' / '45.6K' / '161' → int"""
    s = s.strip().replace(",", "").upper()
    if s.endswith("M"): return int(float(s[:-1]) * 1_000_000)
    if s.endswith("K"): return int(float(s[:-1]) * 1_000)
    return int(s)


def clean_username(raw: str) -> str:
    raw = raw.strip().rstrip("/").lstrip("@")
    m = re.search(r"instagram\.com/([A-Za-z0-9_.]+)", raw)
    return m.group(1) if m else raw


@app.route("/quick_scrape", methods=["POST"])
def quick_scrape():
    raw = (request.get_json(silent=True) or {}).get("url", "").strip()
    if not raw:
        return jsonify({"error": "url is required"}), 400

    username = clean_username(raw)
    url      = f"https://www.instagram.com/{username}/"

    try:
        resp = requests.get(url, headers=HEADERS, timeout=12)
    except Exception as e:
        return jsonify({"error": str(e)}), 502

    if resp.status_code == 404:
        return jsonify({"error": "Profile not found or private."}), 404
    if resp.status_code != 200:
        return jsonify({"error": f"Instagram returned {resp.status_code}"}), 502

    # Extract meta description — Instagram puts content BEFORE name:
    # <meta content="66 Followers..." name="description" />
    html = resp.text
    desc = (
        re.search(r'<meta\s+content=["\'](.*?Follower.*?)["\']\s+name=["\']description["\']', html, re.I) or
        re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']',           html, re.I) or
        re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']',           html, re.I) or
        re.search(r'<meta\s+property=["\']og:description["\']\s+content=["\'](.*?)["\']',    html, re.I)
    )
    if not desc:
        return jsonify({"error": "Could not read stats — profile may be private."}), 422

    desc_text = desc.group(1)

    # Parse all numbers next to Follower / Following / Post
    nums  = re.findall(r"([\d,.]+[KkMm]?)\s+(Follower|Following|Post)", desc_text, re.I)
    stats = {lbl.lower(): parse_num(n) for n, lbl in nums}

    # Extract display name from og:title: "chris_d (@chris_d1969) • Instagram"
    title     = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\'](.*?)["\']', resp.text, re.I)
    full_name = ""
    if title:
        fn = re.match(r"^(.+?)\s*\(", title.group(1))
        if fn:
            full_name = fn.group(1).strip()

    return jsonify({
        "username":    username,
        "full_name":   full_name,
        "followers":   stats.get("follower"),
        "following":   stats.get("following"),
        "posts":       stats.get("post"),
        "profile_url": url,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)