def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

# The time complexity of binary search O(log n).


# =========== Binary search with recursion =========== 

def binaryseaarch_recursive(A, key, l, r):
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binaryseaarch_recursive(A,key,l,mid-1)
        elif key > A[mid]:
            return binaryseaarch_recursive(A,key,mid+1,r)

result = binaryseaarch_recursive(arr, x, 0 , len(arr)-1)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")