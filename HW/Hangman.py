
import random

words = ["spooky", "halloween", "pumpkin"]

target = random.choice(words)
lives = 6
progress = ['_'] * len(target)
guessed = []

print(*progress)

running = True

while running:
    guess = input("Enter a character: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue
    if guess in guessed:
        print("You already guessed that letter!")
        continue
    guessed.append(guess)
    if guess not in target:
        print("Wrong guess!")
        lives -= 1
    else:
        print("Correct guess!")
        for i in range(len(target)):
            if target[i] == guess:
                progress[i] = guess
    print(*progress)
    print("Lives remaining:", lives)
    if '_' not in progress:
        running = False
        print("You win!")
    elif lives == 0:
        running = False
        print("You lose!")
        print("The word was:", target)
