#  Divide and conquer algorithm.

element = [8,10,4,9,6]


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left_arr = myList[:mid]
        right_arr = myList[mid:]
        print('left : ', left_arr , ' Right : ', right_arr)

    # Getting to individual elements to sort via recurssion.
        mergeSort(left_arr)
        mergeSort(right_arr)

        left_index = 0
        right_index = 0

        counter_to_populate_new_array = 0

        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] <= right_arr[right_index]:
                myList[counter_to_populate_new_array] = left_arr[left_index]
                left_index += 1
            else:
                myList[counter_to_populate_new_array] = right_arr[right_index]
                right_index += 1
            counter_to_populate_new_array += 1

        # If length is odd the for uncompared values
        while left_index < len(left_arr):
            myList[counter_to_populate_new_array] = left_arr[left_index]
            left_index += 1
            counter_to_populate_new_array += 1

        while right_index < len(right_arr):
            myList[counter_to_populate_new_array] = right_arr[right_index]
            right_index += 1
            counter_to_populate_new_array += 1

        # print(myList)
    return myList

print(mergeSort(element))


# Worst complexity: n*log(n)
# Average complexity: n*log(n)
# Best complexity: n*log(n)
# Space complexity: n