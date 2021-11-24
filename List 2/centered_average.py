def centered_average(arr):
    result = arr.count(arr[0]) == len(arr)
    if result:
        return arr[0]

    a = min(arr)
    b = max(arr)
    arr.remove(a)
    arr.remove(b)
    return sum(arr)//len(arr)


print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
print(centered_average([7, 7, 7]))
