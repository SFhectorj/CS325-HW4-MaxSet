def max_independent_set(nums):
    """
    This function will return a list with the max sum possible without consecutive numbers.
    """

    # If the given list is empty, return an empty list.
    if nums == 0:
        return []

    # If all numbers are negative, return an empty list.
    if all(number < 0 for number in nums):
        return []

    # Variable to get the number of elements in the list
    n = len(nums)

    # the max_sum holds the maximum sum up to index i
    max_sum = [0] * n   # max_sum[i]

    # This variable will store the elements
    elements_selected = [[] for j in range(n)]

    # Basecase1: Begin with initializing the first element
    max_sum[0] = max(0, nums[0])





