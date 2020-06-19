#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n) Runtime complexity, the running time or space time will grow linearly (at the same rate) and in direct proportion to input size. Has one loop where n increases linearly.


b) O(n^2) for runtime complexity, since there are two loops/iterations taking place over n. 


c) The runtime complexity is constant O(n). Recursion of n in a linear fashion. 



## Exercise II

U

-f standing for limit, kind of like middle index between eggs being broken and not broken 
-want to find the lowest floor number, in which the number of eggs that have been dropped and then are broken will be minimized

-if thrown of of  f >= floor then eggs dropped will be broken
-if thrown of floor f < floor then eggs dropped will not be broken

P
-think about dividing our search to find f value in half, since f is kind of like the middle index. 
-use Binary Search Tree Algorithm, which implies that the data has been sorted

E
-create a function that will take in an array and defined parameters of target- the target value we want
low, and high

    def floor_min(arr, target, low, high):

-create a middle variable using the middle index formula
    middle = (low + high)//2

conditions: 
If the array is empty return -1

if len(arr) == 0:
        return -1

if the middle index in the array is the target then return the middle

if arr[middle] == target:
        return middle

elif the target is less than the middle index, we can       -eliminate the right side
    -use recursion to call our function 
    -have our search start at less than middle at -1

elif arr[middle] > target:
        return floor_min(arr, target, end, middle -1)

else
    if the target value is greater than the middle index, then we can eliminate the left side
    -and call recursion, to have our search start at greater than middle +1

else arr[middle] > target:
        return floor_min(arr, target, end, middle +1)

R

-runtime complexity is O (logn) since we are using a Binary Search Tree 

