from typing import List


def extract_numbers(items: list[object]) -> list[int | float]:
    """Return numeric values from a mixed list.

    Converts numeric strings (e.g. '80' or '9.5') to numbers and ignores non-numeric values.
    """
    nums: list[int | float] = []
    for item in items:
        if isinstance(item, (int, float)):
            nums.append(item)
        elif isinstance(item, str):
            s = item.strip()
            # Try to parse as int first, then float; skip if both fail
            try:
                if "." in s:
                    val = float(s)
                else:
                    val = int(s)
            except ValueError:
                try:
                    val = float(s)
                except ValueError:
                    continue
            nums.append(val)
    return nums


if __name__ == "__main__":
    amounts = [10, "hundred", "80", 450, 9.50]
    numbers = extract_numbers(amounts)
    print(numbers) 
