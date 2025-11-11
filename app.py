def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def main() -> None:
    """Run a simple demo."""
    sum_result = add(2, 3)
    product_result = multiply(2, 3)
    print(f"2 + 3 = {sum_result}")
    print(f"2 * 3 = {product_result}")


if __name__ == "__main__":
    main()  # Entry point
