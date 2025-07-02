def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}"!

def add_numbers(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    print(greet("World"))  # Output: Hello, World!
    print(add_numbers(5, 3))  # Output: 8