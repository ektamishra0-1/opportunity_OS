import requests
from database.models import Observation


REPOS = [
    "pallets/flask",
    "django/django",
    "fastapi/fastapi"
]

HEADERS = {
    "User-Agent": "OpportunityOS/1.0"
}


def fetch_github_issues(limit_per_repo=10):
    observations = []

    print("\n==============================")
    print("[GitHub Agent] STARTING FETCH")
    print("==============================\n")

    for repo in REPOS:
        url = f"https://api.github.com/repos/{repo}/issues"

        print(f"[GitHub] Fetching repo: {repo}")

        response = requests.get(url, headers=HEADERS)

        print(f"[GitHub] Status: {response.status_code}")

        if response.status_code != 200:
            print("[GitHub ERROR]", response.text[:200])
            continue

        issues = response.json()

        print(f"[GitHub] Raw items received: {len(issues)}")

        count_added = 0

        for issue in issues[:limit_per_repo]:

            # DEBUG: show every title
            print(f"[GitHub] ISSUE TITLE: {issue.get('title')}")

            obs = Observation(
                source="github",
                source_id=str(issue.get("id")),
                title=issue.get("title", "") or "",
                content=issue.get("body") or "",
                author=(issue.get("user") or {}).get("login", ""),
                url=issue.get("html_url"),
                timestamp=issue.get("created_at", "")
            )

            observations.append(obs)
            count_added += 1

        print(f"[GitHub] Added from {repo}: {count_added}")

    print("\n==============================")
    print("[GitHub Agent] FINAL SUMMARY")
    print(f"TOTAL OBSERVATIONS CREATED: {len(observations)}")
    print("==============================\n")

    return observations