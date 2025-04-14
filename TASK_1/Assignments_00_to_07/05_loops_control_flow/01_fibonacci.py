
MAX_TERM_VALUE = 15  # Max limit define 


def main():
    curr_term, next_term = 0, 1  # Pehle do Fibonacci numbers
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print without new line
        curr_term, next_term = next_term, curr_term + next_term  # Update values

if __name__ == '__main__':
    main()

