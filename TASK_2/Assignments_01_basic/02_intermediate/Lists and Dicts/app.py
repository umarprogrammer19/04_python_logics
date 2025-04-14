# Problem #1: List Practice

def main():
    # Step 1: List of banana
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    print("Length of the list:", len(fruit_list))

    fruit_list.append('mango')

    print("Updated List:", fruit_list)

main()


# Problem #2: Index Game


def access_element(my_list, index):
    """List ke element ko access karne ka function"""
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    else:
        return "Invalid index! Out of range."



def modify_element(my_list, index, new_value):
    """List ke kisi element ko modify karne ka function"""
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"Updated list: {my_list}"
    else:
        return "Invalid index! Out of range."




def slice_list(my_list, start, end):
    """List ka ek part (slice) return karne ka function"""
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list) and start < end:
        return f"Sliced list: {my_list[start:end]}"
    else:
        return "Invalid indices for slicing!"


def main():
    my_list = [10, 'apple', 25.5, 'banana', 100]


    while True:
        print("\nOptions:")
        print("1: Access an element")
        print("2: Modify an element")
        print("3: Slice the list")
        print("4: Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            index = int(input("Enter the index: "))
            print(access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter the index: "))
            new_value = input("Enter the new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))

        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

main()
