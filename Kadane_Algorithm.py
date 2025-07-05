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

inp = [-2,1,-3,4,-1,2,1,-5,4]

start = 0
end = 1
max_val = inp[0]

for i in range(len(inp)):
    for j in range(i + 1, len(inp) + 1):  # j goes 1 past end
        temp_sum = inp[i:j]
        if sum(temp_sum) > max_val:
            max_val = sum(temp_sum)
            start, end = i, j


print(inp[start:end], max_val)

# ========================================================================

# variable sliding window

max_sum = inp[0]
start = 0
end = 0
sum = max_sum
for i in range(len(inp)):
    sum = sum + inp[i]

    if sum < 0:
        start = i+1
        sum = 0
    if sum > max_sum:
        end = i+1
        max_sum = sum

print(inp[start: end] ,max_sum)


