def add_many_numbers(numbers: list[int]) -> int:
    """Returns the sum of a list of numbers without using built-in methods."""
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers = [1, 2, 3, 4, 5,6]  # List of numbers
    print(add_many_numbers(numbers))  # Print sum

if __name__ == '__main__':
    main()
