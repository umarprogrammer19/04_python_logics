def main():
    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
    for i in range(20):
        print(i * 2)  # Use the 'i' value inside the for-loop
   
# Call the main function when "run", no need to edit anything below!
if __name__ == "__main__":
    main()


def main():
    num = 0  # Pehla even number
    count = 0  # 20 numbers tak count karne ke liye

    while count < 20:
        print(num, end=" ")
        num += 2  # Next even number
        count += 1  # Count increase karna zaroori hai

if __name__ == "__main__":
    main()
