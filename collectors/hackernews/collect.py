import requests
from database.models import Observation


def fetch_hn_top_stories(limit=50):
    story_ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json"
    ).json()

    observations = []

    for story_id in story_ids[:limit]:
        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        ).json()

        if not item:
            continue

        observations.append(Observation(
            source="hackernews",
            source_id=str(item.get("id")),
            title=item.get("title", ""),
            content=item.get("text", "") or "",
            author=item.get("by", ""),
            url=item.get("url", f"https://news.ycombinator.com/item?id={story_id}"),
            timestamp=str(item.get("time", ""))
        ))

    return observations