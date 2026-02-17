"""Standard deviation utility.

Provides a function to compute population or sample standard deviation.
"""
from typing import Iterable, List


def standard_deviation(values: Iterable[float], sample: bool = False) -> float:
    """Return the standard deviation of the numbers in `values`.

    Args:
        values: Iterable of numeric values.
        sample: If True, compute the sample (unbiased) standard deviation
                dividing by (n-1). If False (default), compute the population
                standard deviation dividing by n.

    Raises:
        ValueError: if values is empty or sample=True but fewer than 2 points.
    """
    values: List[float] = list(values)
    n = len(values)
    if n == 0:
        raise ValueError("standard_deviation requires at least one data point")
    if sample and n < 2:
        raise ValueError("sample standard deviation requires at least two data points")

    mean = sum(values) / n
    var_sum = sum((x - mean) ** 2 for x in values)
    variance = var_sum / (n - 1) if sample else var_sum / n
    return variance ** 0.5


if __name__ == "__main__":
    # Simple demonstration
    data = [1, 2, 3, 4, 5]
    print("Data:", data)
    print("Population standard deviation:", standard_deviation(data))
    print("Sample standard deviation:", standard_deviation(data, sample=True))
