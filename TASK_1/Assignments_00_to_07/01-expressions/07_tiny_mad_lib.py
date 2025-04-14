SENTENCE_START = "Exploring Python is exciting! Today, I built a "  

def main():
    # Get user inputs
    adj = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    # Print the final sentence
    print(f"{SENTENCE_START}{adj} {noun} that can {verb}!")

if __name__ == '__main__':
    main()
