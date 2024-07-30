import random

def montyHall():
    door = ['0', '0', '1']
    choice = random.randint(0, 2)
    reveals = random.choice([i for i in range(3) if i != choice and door[i] == '0'])
    switchChoice = random.choice([True, False])

    if switchChoice:
        choice = next(i for i in range(3) if i != choice and i != reveals)

    return door[choice] == '1'


wins = sum(montyHall() for _ in range(10000))
win_percentage = (wins / 10000) * 100
print(f"Процент побед после 10000 попыток: {win_percentage}%")