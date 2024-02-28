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

def binary_search(L, start, end, item):  
    if end >= start:  
        middle = (start + end) // 2  
        if L[middle] == item:  
            return middle #middle element is the item to be located  
        #if middle item is greater than the item to be searched, left side of the list will be searched  
        elif L[middle] > item:   
            #starting index will be same but ending index will be the middle of the main list i.e. left half of the list is given in function.  
            return binary_search(L, start, middle - 1, item)  
        else:  
            #if middle item is smaller than the item to be searched, new starting index will be middle of the list i.e. right half of the list.  
            return binary_search(L, middle + 1, end, item)  
    else:  
        #if element is not present in the list  
        return -1

my_list = [ 2, 4, 6, 9, 12, 16, 18, 19, 20, 21, 22 ]  
element_to_search = 6  
print("The given list is")  
print(my_list)  
  
index_of_element = binary_search(my_list, 0, len(my_list)-1, element_to_search)  
  
if index_of_element != -1:  
    print("Element searched is found at the index ", str(index_of_element), "of given list")  
else:  
    print("Element searched is not found in the given list!")  
