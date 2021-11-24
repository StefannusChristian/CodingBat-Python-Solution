def count_evens(nums):
    even = [i for i in nums if i % 2 == 0]
    return len(even)
