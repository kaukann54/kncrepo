def subtract(a, b):
    """
    Subtracts two numbers and returns the result.
    Handles cases where inputs are not numbers.
    """
    try:
        return a - b
    except TypeError:
        return "Inputs must be numbers."

if __name__ == "__main__":
    # Test cases
    print(f"Difference (15, 5): {subtract(15, 5)}")
    print(f"Difference (15, '5'): {subtract(15, '5')}")
