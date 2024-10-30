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
    # Any number less than 0 cannot continue
    if max_sum[0] > 0:
        elements_selected[0].append((nums[0]))

    # Basecase2: Now it initializes the second element
    if n > 1:
        # Take the largest between the first and second element
        max_sum[1] = max(max_sum[0], nums[1])

        # When nums[1] is chosen over the first element
        if max_sum[1] == nums[1]:
            elements_selected[1].append(nums[1])
        else:
            # otherwise the first element will be copied
            elements_selected[1] = elements_selected[0]

    # Process the remaining elements
    for i in range(2, n):
        # Option 1: Exclude nums[i] (take max_sum[i-1])
        if max_sum(i - 1) > max_sum[i - 2] + nums[i]:
            max_sum[i] = max_sum[i - 1]
            elements_selected[i] = elements_selected[i - 1]
        else:
            # Option 2: Include nums[i] (take max_sum[i-2] + nums[i])
            max_sum[i] = max_sum[i - 2] + nums[i]
            elements_selected[i] = elements_selected[i - 2] + [nums[i]]

    # Return the maximum result at the last position
    return elements_selected[-1]






