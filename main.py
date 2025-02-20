from utils import factorial, is_prime, is_power_of_5, is_power_of_2

def main():
    # Test factorial function
    print("Testing factorial function:")
    for n in range(5):
        print(f"factorial({n}) = {factorial(n)}")
    
    # Test is_prime function
    print("\nTesting is_prime function:")
    for n in range(10):
        print(f"{n} is{' ' if is_prime(n) else ' not '}prime")
    
    # Test is_power_of_5 function
    print("\nTesting is_power_of_5 function:")
    test_numbers = [1, 5, 25, 125, 24, 26]
    for n in test_numbers:
        print(f"{n} is{' ' if is_power_of_5(n) else ' not '}a power of 5")
    
    # Test is_power_of_2 function
    print("\nTesting is_power_of_2 function:")
    test_numbers = [1, 2, 4, 8, 16, 15, 17]
    for n in test_numbers:
        print(f"{n} is{' ' if is_power_of_2(n) else ' not '}a power of 2")

if __name__ == "__main__":
    main()
