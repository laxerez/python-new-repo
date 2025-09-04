def average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)

def median(numbers: list[float]) -> float:
    """Calculate the median of a list of numbers."""
    n = len(numbers)
    if n == 0:
        raise ValueError("List is empty")
    sorted_nums = sorted(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print(f"Average: {average(data)}")
    data = [10, 20, 30, 40, 50]
    print(f"Median: {median(data)}")
