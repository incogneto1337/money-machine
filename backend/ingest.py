import feedparser, json
from datetime import datetime

FEEDS = ["https://news.ycombinator.com/rss"]

def fetch():
    items = []
    for url in FEEDS:
        feed = feedparser.parse(url)
        for e in feed.entries[:5]:
            items.append({
                "title": e.title,
                "summary": e.get("summary", ""),
                "url": e.link
            })

    payload = {
        "source": "rss",
        "fetched_at": datetime.utcnow().isoformat(),
        "items": items
    }

    with open("data/raw.json", "w") as f:
        json.dump(payload, f, indent=2)

if __name__ == "__main__":
    fetch()