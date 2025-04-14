def read_phone():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}

    while True:
        name = input("Enter Name: ")
        if name == "":
            break

        number = input("Enter Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phone):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phone:
        print(f"{name} ---> {phone[name]}")


def lookup_num(phone):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup:👀 ")
        if name == "":
            break
        if name not in phone:
            print(f"{name} is not in the phonebook❌")
        else:
            print(f"Number✅ : {phone[name]}")


def main():
    """
    Main function to read phone numbers, print the phonebook,
    and allow the user to look up numbers.
    """
    phonebook = read_phone()
    print_phonebook(phonebook)
    lookup_num(phonebook)


if __name__ == '__main__':
    main()
