import random

def main():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")

    while True:
        guess = int(input("Enter a guess: "))

        if guess == secret_number:
            print(f"Congrats! The number was: {secret_number}")
            break
        elif abs(secret_number - guess) <= 5:
            print("Very close!")
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

if __name__ == '__main__':
    main()
