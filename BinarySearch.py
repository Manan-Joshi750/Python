def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 

arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
n = int(input("Enter any target value : "))
result = binary_search(arr, n)
if result >= 0 :
    print(f"Target value {n} is found in the array at index {result}")
else :
    print(f"Target value {n} is not found in the array")