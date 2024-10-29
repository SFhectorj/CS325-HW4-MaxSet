def max_independent_set(nums):
    """
    This function will return a list with non-consecutive numbers
    """

    # Basecase1: If the given list is empty, return an empty list.
    if nums == 0:
        return []

    # Basecase2: If all numbers are negative, return an empty list.
    if all(number < 0 for number in nums):
        return []




