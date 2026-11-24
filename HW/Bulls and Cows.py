
import random
def show_instructions():
    print("Welcome to the Bulls and Cows game. Here are the rules: A secret four digit code will be generated, and you need to guess. Now remember: Bulls=right digit, right spot, Cows=right digit, wrong spot. Enjoy!")

def generate_code():
    code = []
    while len(code) < 4:
        digit = random.randint(0, 9)
        if digit not in code:
            code.append(digit)
    return code

def get_guess():
    guess = []
    while len(guess) < 4:
        digit = int(input("Enter a digit (0-9): "))
        guess.append(digit)
    return guess

def has_duplicates(numbers):
    return len(numbers) != len(set(numbers))

def is_valid_guess(guess):
    if len(guess) != 4:
        return False
    if has_duplicates(guess):
        return False
    for digit in guess:
        if digit < 0 or digit > 9:
            return False
    return True

def count_bulls(secret, guess):
    bulls = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
    return bulls

def count_cows(secret, guess):
    cows = 0
    for i in range(len(secret)):
        if guess[i] in secret and guess[i] != secret[i]:
            cows += 1
    return cows

def show_result(bulls, cows):
    print("Bulls:", bulls)
    print("Cows:", cows)

def has_won(bulls):
    if bulls == 4:
        return True
    else:
        return False

def show_final_message(attempts):
    print("Congratulations!")
    print(f"You guessed the secret in {attempts} attempts!")

def main():
    show_instructions()
    secret = generate_code()
    attempts = 0
    won = False

    while not won:
        print()
        print("--------------------------")
        print("Attempt:", attempts + 1)

        guess = get_guess()

        while not is_valid_guess(guess):
            print("Invalid guess! Please try again.")
            guess = get_guess()

        attempts += 1

        bulls = count_bulls(secret, guess)
        cows = count_cows(secret, guess)

        show_result(bulls, cows)
        won = has_won(bulls)

    show_final_message(attempts)

main()
