# TO-DO: Complete the selection_sort() function below
# TC stands for time complexity - how long does it take to run this a function
# SC stands for space complexity - how much extra space do we need to allocate in space to run a function

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr) - 1):                       # TC: O(n) # Range defaults to start at zero if you don't give it an initial position
        cur_index = i                                   # TC: O(1) # SC: O(1)
        smallest_index = cur_index                      # TC: O(1) # SC: O(1)
        # TO-DO: find next smallest element
        # (hint, can do in 3 lines of code )
        for j in range(cur_index, len(arr)):            # TC: O(log n) - goes through less and less of the lenght of thet array each time # It's only len(arr) and not len(arr) - 1 becuase we need it to compare one thing further?
            if arr[j] < arr[smallest_index]:            # TC: O(1)
                smallest_index = j                      # TC: O(1) # SC: O(1)

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]       # TC: O(1)

    return arr
    
    # Time Complexity: 
    # (n)(1 + 1 + log n)(1 + 1)
    # n * 2 log n * 2
    # 2n * 2log n
    # Final Time Complexity: O(n log n)

    # Space Complexity:
    # 1 + 1 + 1
    # Final Space Complexity: O(1)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr) - 1):                       # TC: O(n)      # this will loop through the length of the array
        for j in range(len(arr) - 1 - i):               # TC: O(log n)  # this will loop from the beginning until the last one - i value - the shorter array 
            if arr[j] > arr[j + 1]:                     # TC: O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # TC: O(1)

    return arr

# Final Time Complexity: O(n log n)
# Final Space Complexity: O(1) # We are not creating a new variable - we don't use up any new space

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
