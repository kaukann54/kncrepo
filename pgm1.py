def add(a, b):
    """
    Adds two numbers and returns the result.
    Handles cases where inputs are not numbers.
    """
    try:
        return a + b
    except TypeError:
        return "Inputs must be numbers."

if __name__ == "__main__":
    # Test the function with valid inputs
    print(f"Sum (5, 10): {add(5, 10)}")
    
    # Test the function with invalid inputs
    print(f"Sum (5, '10'): {add(5, '10')}")
