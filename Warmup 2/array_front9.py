def array_front9(nums):
    if len(nums) < 4:
        if 9 in nums:
            return True

    front = nums[:4]
    if 9 in front:
        return True
    return False
