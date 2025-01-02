def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

if __name__ == "__main__":
    print(f"Quotient: {divide(20, 4)}")
