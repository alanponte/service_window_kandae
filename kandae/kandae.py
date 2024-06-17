"""
"standard" implementation of Kandae's Algorithm.
https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""
from typing import Tuple


MAX_SIZE = int(1e9+7)


def smallest_sum_subarr(arr) -> Tuple[int, int, int]:
    """Return the sum of the smallest contiguous subarray as well as the
    indexes of the subarray.

    :param arr: Array.
    :return: A tuple, whose first element is the sum, and the second and third elements are the indexes.
    """
    # to store the minimum value that is ending
    # up to the current index
    min_ending_here = MAX_SIZE

    # to store the minimum value encountered so far
    min_so_far = MAX_SIZE

    # to store the starting index of the minimum subarray
    start = 0

    # to store the ending index of the minimum subarray
    end = 0

    # temporary start index for the current subarray
    s = 0

    n = len(arr)
    # traverse the array elements
    for i in range(n):
        # if min_ending_here > 0, then it could not possibly
        # contribute to the minimum sum further
        if min_ending_here > 0:
            min_ending_here = arr[i]
            s = i  # start a new subarray
        else:
            min_ending_here += arr[i]

        # update min_so_far and the indexes
        if min_so_far > min_ending_here:
            min_so_far = min_ending_here
            start = s
            end = i

    # return the smallest sum and the subarray indexes
    return min_so_far, start, end

