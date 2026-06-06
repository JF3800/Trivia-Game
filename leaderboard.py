import json
import os

def save_score(name, score):
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r") as f:
            scores = json.load(f)
    else:
        scores = []

    scores.append({"name": name, "score": score})

    with open("leaderboard.json", "w") as f:
        json.dump(scores, f)

def show_leaderboard():
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r") as f:
            scores = json.load(f)
        for entry in scores:
            print(f"{entry['name']}: {entry['score']}")
    else:
        print("No scores yet!")