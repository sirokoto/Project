def load_high_score():
    try:
        with open('highscore.txt', 'r') as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
    return high_score

def save_high_score(high_score):
    with open('highscore.txt', 'w') as file:
        file.write(str(high_score))
