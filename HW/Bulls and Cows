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
        guess.append(int(input("Enter a digit (0-9): ")))
    return guess
def has_duplicates(numbers):

def is_valid_guess(guess):
    pass
def count_bulls(secret, guess):
    bulls = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
    return bulls
def count_cows(secret, guess):
    cows = 0
    for i in range(len(secret)):
        if secret[i] != guess[i]:
            cows += 1
    return cows
    pass
def show_result(bulls, cows):
    print(bulls, cows)
    pass
def has_won(bulls):
    if bulls == 4:
        return True
    else:
        return False
    # ---------------------------------------------------------
# Function 10: Display the final message
# ---------------------------------------------------------
def show_final_message(attempts):
    print("Congratulations!")
    print(f"You guessed the secret in {attempts} attempts!")
def main():
show_instructions()
secret = generate_secret()
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
def show_final_message(attempts):
    print("Congratulations!")
    print("You guessed the secret in", attepmts, "attempts!")
main()
