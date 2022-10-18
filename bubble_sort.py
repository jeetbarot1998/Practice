elements = [9,8,6,4]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            print('j',j)
            print('j+1',j+1)
            print('arr',arr)
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
                print('arr',arr)

bubble_sort(elements)

# Worst complexity: n^2
# Average complexity: n^2
# Best complexity: n
# Space complexity: 1