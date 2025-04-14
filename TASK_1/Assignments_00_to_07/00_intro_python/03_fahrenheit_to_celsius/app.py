
def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()
