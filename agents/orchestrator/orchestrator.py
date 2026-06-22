import time

from collectors.github.collect import fetch_github_issues
from collectors.hackernews.collect import fetch_hn_top_stories
from database.db import insert_observation


class OrchestratorAgent:
    def __init__(self):
        self.cycle_count = 0

    def run_cycle(self):
        print("\n==============================")
        print(f"ORCHESTRATOR CYCLE: {self.cycle_count}")
        print("==============================\n")

        all_observations = []

        # 1. Run Source Agents
        print("[Agent] GitHub Agent running...")
        github_obs = fetch_github_issues()
        all_observations += github_obs
        print(f"GitHub → {len(github_obs)} observations")

        print("[Agent] HackerNews Agent running...")
        hn_obs = fetch_hn_top_stories()
        all_observations += hn_obs
        print(f"HN → {len(hn_obs)} observations")

        # 2. Store in Memory
        print("\n[Memory] Storing observations...")

        stored = 0
        for obs in all_observations:
            insert_observation(obs)
            stored += 1

        print(f"[Memory] Stored {stored} observations")

        self.cycle_count += 1

        print("\n[CYCLE COMPLETE]\n")

    def run_forever(self, delay_seconds=60):
        print("Starting Orchestrator Agent...\n")

        while True:
            self.run_cycle()
            time.sleep(delay_seconds)