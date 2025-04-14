ADULT_AGE: int = 18 

def is_adult(age: int):
    return bool(age >= ADULT_AGE)  # Boolean Conversion 

def main():
    age: int = int(input("How old is this person?: "))  
    print(is_adult(age))  

if __name__ == "__main__":
    main()
