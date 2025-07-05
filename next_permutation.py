# https://www.youtube.com/watch?v=JDOXKqF60RQ

"""
Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

Example 1 :

Input format: Arr[] = {1,3,2}
Output: Arr[] = {2,1,3}
Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.
Example 2:

Input format: Arr[] = {3,2,1}
Output: Arr[] = {1,2,3}
Explanation: As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the topmost permutation.
"""

def get_next_perm(lis):
    ind = -1
    # Find where the breakpoint occurs
    for i in range(len(lis)-2, -1, -1):
        if lis[i] < lis[i+1]:
            ind = i

    # Check if breakpoint exists or not
    if ind == -1:
        return lis[::-1]

    # If exists, exchange 1st higher number than the breakpoint with breakpoint index
    for i in range(len(lis)-1, ind, -1):
        if lis[i] > lis[ind]:
            lis[ind], lis[i] = lis[i], lis[ind]
            break

    # rotate after breakpoint index and extend and return
    lis[:ind].extend((lis[ind + 1:])[::-1])
    return lis


print(get_next_perm([2,1,5,4,3,0,0]))
# ans = 2,3,0,0,1,4,5
