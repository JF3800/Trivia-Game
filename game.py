from leaderboard import save_score, show_leaderboard
import requests
import html

def fetch_questions(amount=10):
    url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
    response = requests.get(url)
    data = response.json()

    questions = []
    for item in data["results"]:
        question = {
            "question": html.unescape(item["question"]),
            "correct": html.unescape(item["correct_answer"]),
            "choices": [html.unescape(a) for a in item["incorrect_answers"] + [item["correct_answer"]]]
        }
        question["choices"].sort()
        questions.append(question)

    return questions

def run_game():
    questions = fetch_questions()
    score = 0
    for question in questions:
        print(question["question"])
        for i, choice in enumerate(question["choices"],1):
            print(str(i) + ") " + choice)
        answer = input("Which choice do you pick? Pick the corrosponding number: ")
        answer = question["choices"][int(answer)- 1 ]
        if answer == question["correct"]:
            print("CORRECT! :) ")
            score += 1
            print(f"Score + 1 | Current Score: {score}")
        else:
            print("incorrect :/")
            print(f"Current Score:{score}")
    print(f"Final Score: {score}")
    name = input("what is your name?")
    save_score(name, score)
run_game()
