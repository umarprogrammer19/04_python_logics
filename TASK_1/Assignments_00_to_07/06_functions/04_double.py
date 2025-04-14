def double(num:int):
    return num * 2

def main():
    user_in = int(input("Enter a number"))
    num_time_2 = double(user_in)
    print(num_time_2)


if __name__ == '__main__':
    main()