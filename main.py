import random
def prompt_n():
    while True:
        try:
            n = int(input("Guess a number: "))
            return n
        except ValueError:
            print("That's not a number. Try again.")

random_number = random.randint(1, 10)
while True:
    n = prompt_n()
    if n == random_number:
        print("You guessed correctly.")
        print("Game ends")
        break
    elif n < random_number:
        print("Too small. ")
    elif n > random_number:
        print("Too big.")
    

