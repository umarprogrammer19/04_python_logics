
def get_user_numbers():
    user_num = []

    while True:
        user_input = input('Enter a number')

        if user_input == "":
            break

        num = int(user_input)
        user_num.append(num)
    return user_num
        



def count_nums(num_lst):

    num_dict = {}

    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    return num_dict



def print_counts(num_dict):
    for num in num_dict:
        print(f"{num} apppers in {num_dict[num]} times!!")



def main():
    user_numbers = get_user_numbers()
    count = count_nums(user_numbers)
    print_counts(count)
    
if __name__ == "__main__":
    main()
