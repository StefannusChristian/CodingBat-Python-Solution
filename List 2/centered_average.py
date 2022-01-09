def centered_average(arr):
    result = arr.count(arr[0]) == len(arr)
    if result:
        return arr[0]
    a = min(arr)
    b = max(arr)
    arr.remove(a)
    arr.remove(b)
    return sum(arr)//len(arr)
