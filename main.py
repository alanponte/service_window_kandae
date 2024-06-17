from kandae.kandae import smallest_sum_subarr, smallestSubArrayLen


def main():
    # arr = [3, -4, 2, -3, -1, 7, -5]
    # print(f'INPUT: {arr}')
    # print(smallest_sum_subarr(arr))

    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(f'INPUT: {nums}, TARGET: {target}')
    print(smallestSubArrayLen(target, nums))


if __name__ == '__main__':
    main()
