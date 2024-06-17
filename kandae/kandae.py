"""
"standard" implementation of Kandae's Algorithm.
https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""
from bisect import bisect_left
from typing import Tuple, List

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


def smallestSubArrayLen(target: int, nums: List[int]) -> Tuple[int, int]:
    """
    Return the length of the smallest contiguous subarray with a sum greater than the target value,
    and the start and end indexes of that subarray.

    :param target: Target sum value.
    :param nums: List of numbers.
    :return: A tuple, whose first element the start index of the subarray, and the second element
             is the end index of the subarray. If no such subarray exists, return (-1, -1).
    """
    n = len(nums)
    # No valid subarray.
    if n == 0:
        return -1, -1

    ans = float('inf')
    start_index = -1
    end_index = -1

    sums = [0] * (n + 1)
    for i in range(1, n + 1):
        sums[i] = sums[i - 1] + nums[i - 1]

    for i in range(1, n + 1):
        to_find = target + sums[i - 1]
        bound = bisect_left(sums, to_find)
        if bound != len(sums):
            length = bound - (i - 1)
            if length < ans:
                ans = length
                start_index = i - 1
                end_index = bound - 1

    return (start_index, end_index) if ans != float('inf') else (-1, -1)
