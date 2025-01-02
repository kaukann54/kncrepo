def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    Handles cases where inputs are not numbers.
    """
    try:
        return a * b
    except TypeError:
        return "Inputs must be numbers."

if __name__ == "__main__":
    # Test cases
    print(f"Product (3, 7): {multiply(3, 7)}")
    print(f"Product (3, '7'): {multiply(3, '7')}")
