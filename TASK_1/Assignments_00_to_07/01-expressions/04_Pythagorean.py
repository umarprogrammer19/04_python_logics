import math  # For sqrt function

def main():
    ab = float(input("Enter length of AB: "))
    ac = float(input("Enter length of AC: "))
    print(f"The length of BC (hypotenuse) is: {math.sqrt(ab**2 + ac**2)}")

if __name__ == '__main__':
    main()
