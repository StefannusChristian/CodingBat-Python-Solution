def sum13(nums):
    if len(nums) == 0:
        return 0
    for i in range(len(nums)-1):
        if nums[i] == 13:
            nums[i+1] = 0
    while 13 in nums:
        nums.remove(13)
    return sum(nums)

