C = 299792458  # Speed of light in m/s

def main():
    m = float(input("Enter kilos of mass: "))
    e = m * C**2
    print(f"e = m * C^2...\nm = {m} kg\nC = {C} m/s\n{e} joules of energy!")

if __name__ == '__main__':
    main()
