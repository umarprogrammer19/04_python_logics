AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation:")
    print(AFFIRMATION)

    while True:  # Infinite loop until correct input
        user_input = input()  # User se input lena

        if user_input == AFFIRMATION: 
            print("That's right! :)")
            break
        else:
            print("That was not the affirmation. Please try again!")

if __name__ == "__main__":
    main()
