def in_range(n: int, low: int, high: int) -> bool:
    """ Returns True if n is between low and high (inclusive) """
    return low <= n <= high  # Direct Range Check

# Testing the function
print(in_range(5, 1, 10))   # ✅ True
print(in_range(15, 1, 10))  # ❌ False
print(in_range(10, 1, 10))  # ✅ True (Inclusive)
print(in_range(1, 1, 10))   # ✅ True (Inclusive)
print(in_range(-3, -5, 0))  # ✅ True
