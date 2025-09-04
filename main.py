def average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print(f"Average: {average(data)}")
