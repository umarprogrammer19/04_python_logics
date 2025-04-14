def get_first_element(lst):
    print(lst[0])

def get_lst():
    lst = []
    element: str = input("Enter an element of the list:")
    while not element:
        element = input("Enter at least one element of the list:")
    lst.append(element)
    while True:
        element = input("Enter another element of the list:")
        if element:
            lst.append(element)
        else:
            break
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == "__main__":
    main()
