from database.models import Observation


def collect_posts():
    observations = []

    observation = Observation(
        source="reddit",
        source_id="reddit_001",
        title="Cleaning datasets takes forever",
        content="I spend hours cleaning CSV files.",
        author="reddit_user",
        url="https://reddit.com/test",
        timestamp="2026-06-18"
    )

    observations.append(observation)

    return observations