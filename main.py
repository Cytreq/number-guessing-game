import random
def prompt_n(text):
    while True:
        try:
            n = int(input(text))
            return n
        except ValueError:
            print("That's not a number. Try again.")

def settings():
    scope = prompt_n("Choose the maximum number to guess (e.g., 50): ")
    rounds = prompt_n("How many rounds do you want to play? ")
    return scope, rounds

def play_round(scope):
    random_number = random.randint(1, scope)
    attempts = 0

    while True:
        n = prompt_n("Guess a number: ")
        if not 1 <= n <= scope:
             print(f"Please enter a number between 1 and {scope}")
             continue
        attempts += 1
        if n == random_number:
            print(f"You guessed correctly in {attempts} attempts")
            break
        elif n < random_number:
            print("Too small.")
        else:
            print("Too big.") 
def main():
    scope, rounds = settings()
    for i in range(rounds):
        print(f"Starting round {i+1}.")
        play_round(scope)

if __name__ == "__main__":
    main()
