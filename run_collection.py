from database.db import create_tables, insert_observation
from collectors.reddit.collect import collect_posts

create_tables()

observations = collect_posts()

for observation in observations:
    insert_observation(observation)

print(f"Stored {len(observations)} observations.")