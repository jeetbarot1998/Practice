# https://www.youtube.com/watch?v=AHZpyENo7k4

"""
Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

Examples
Example 1:

Input: arr = [-2,1,-3,4,-1,2,1,-5,4]

Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

Examples 2:

Input: arr = [1]

Output: 1
"""
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = arr[0]
current_sum = 0

start = 0
end = 0
temp_start = 0

for ind, val in enumerate(arr):
    current_sum += val

    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = ind

    if current_sum < 0:
        current_sum = 0
        temp_start = ind + 1

print(start, end, arr[start:end+1], max_sum)



