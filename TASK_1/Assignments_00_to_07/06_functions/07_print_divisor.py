
def print_divisors(num: int):
    print(f"Here are the divisors of {num}\n")
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print("curr_divisor=> ",curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()