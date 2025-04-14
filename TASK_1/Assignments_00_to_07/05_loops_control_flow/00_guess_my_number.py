import random


def guess():
    secret_number = random.randint(1,4)

    print("I am thinking of a number between 1 and 99...")

    guess = int(input("Enter a number: "))
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")

        else:
            print("Your guess is too high")

        print()
        guess = int(input("Enter a new guess: "))
    
    print(f"Congrats!👏 The number was: {str(secret_number)}")


if __name__ == "__main__":
    guess()

    

        



