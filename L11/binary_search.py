def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < target:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

# Перевірка
assert binary_search([11, 12, 22, 25, 34, 64, 90], 22) == 2

print(binary_search([11, 12, 22, 25, 34, 64, 90], 22))