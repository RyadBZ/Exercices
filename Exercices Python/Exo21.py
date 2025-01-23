def length(lst):
    """
    Returns the number of elements in the list.
    """
    return len(lst)

def mean(lst):
    """
    Calculates and returns the arithmetic mean of the list.
    Handles empty list edge case.
    """
    if not lst:
        return None  # Avoid division by zero for an empty list
    return sum(lst) / len(lst)

def range_of_list(lst):
    """
    Returns the difference between the maximum and minimum values in the list.
    Handles empty list edge case.
    """
    if not lst:
        return None
    return max(lst) - min(lst)

def median(lst):
    """
    Calculates and returns the median of the list.
    Handles empty list edge case.
    """
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]

def standard_deviation(lst):
    """
    Calculates and returns the standard deviation of the list.
    Handles empty list edge case.
    """
    if not lst:
        return None
    mean_value = mean(lst)
    variance = sum((x - mean_value) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def list_statistics(lst):
    """
    Creates and returns a dictionary with list statistics:
    length, mean, range, median, and standard deviation.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    return {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst),
    }
if __name__ == "__main__":
    test_lists = {
        "Empty List": [],
        "Single Element": [10],
        "Negative Numbers": [-5, -10, -3],
        "Floating-Point Numbers": [1.2, 2.5, 3.8, 4.1],
        "Mixed Positive and Negative": [-1, 0, 1, 2, 3],
    }

    for description, lst in test_lists.items():
        print(f"\n{description}: {lst}")
        stats = list_statistics(lst)
        for key, value in stats.items():
            print(f"{key}: {value}")