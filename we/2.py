
def read_scores():
    scores = {}
    with open("highscores.txt", "r") as file:
        for line in file:
            name, score = line.strip().split(":")
            scores[name] = int(score)
    return scores

def write_scores(scores):
    with open("highscores.txt", "w") as file:
        for name, score in scores.items():
            file.write(f"{name}:{score}\n")
scores = read_scores()

name = input("Enter name")
score = int(input("Enter score"))

if name in scores:
    if score > scores[name]:
        scores[name] = score
else:
    scores[name] = score
write_scores(scores)
print("\nHigh Scores:")
for player, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{player}: {score}")
