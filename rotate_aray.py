def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)
 
#Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
 
  
# Driver program to test above functions */
arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)

leftRotate(arr, 2, 7)
print(arr)
# printArray(arr, 7)



def rightRotate(arr, d, n):
    for _ in range(d):
        rightRotatebyOne(arr, n)
 
#Function to left Rotate arr[] of size n by 1*/
def rightRotatebyOne(arr, n):
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp

         
rightRotate(arr, 2, 7)
print(arr)

