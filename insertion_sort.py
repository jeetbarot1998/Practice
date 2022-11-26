array = [8,4,6,9,15,12,11]

def InsertionSort(arr):
    for val in range(1,len(arr)):
        b=val
        while b > 0 and arr[b] < arr[b-1]:
            arr[b-1] , arr[b] = arr[b], arr[b-1]
            b -= 1
            print(arr)

InsertionSort(array)

# Worst complexity: n^2
# Average complexity: n^2
# Best complexity: n
# Space complexity: 1