# Function to get the last item in the list
def get_last_element(lst):
    print(lst[-1])


# Function to create a list
def get_lst():
    # Start with an empty list
    lst = []

    # Ask the user for the first item in the list
    element: str = input("Enter an item for the list:")

    # Make sure the user enters at least one item
    while not element:
        element = input("Please enter at least one item for the list:")

    # Add the first item to the list
    lst.append(element)

    # Keep asking for more items until the user stops
    while True:
        # Ask for the next item
        element = input("Enter another item for the list:")

        # Add the item to the list if it's not empty
        if element:
            lst.append(element)
        else:
            break
    return lst


# Main function to run the program
def main():
    # Get the list from the user
    lst = get_lst()

    # Print the last item in the list
    get_last_element(lst)


if __name__ == "__main__":
    main()
