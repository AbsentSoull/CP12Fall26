import random

words = ["spooky", "halloween", "pumpkin"]
# we can have multiple lists
# with various difficulty levels
target = random.choice(words)
print(target)
lives = 6
progress = ['_'] * len(target)
print(*progress)
running = True
while running:
    guess = input("Enter a character: ")
    # validate guess (single character)

    if guess not in target:
        print("Wrong guess!")
        lives -= 1
        if lives == 0:
            running = False
    else:
        for i in range(len(target)):
            if target[i] == guess:
                progress[i] = guess
    if guess == target:
        running = False
    print(*progress)
if guess == target:
    print("You win!")
else:
    print("You lose!")