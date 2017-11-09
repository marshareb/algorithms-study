import math
import time
import random

# Decorator to time functions
def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print(str(method.__name__) + " with k value " + str(args[1]) + " took " + str(te-ts) + " second(s)")
        return result

    return timed


print('Merge function:')


# We first implement our merge function

# Notice we use the merge without sentinel values.
# Let A,B be two different arrays (lists, in this case) both sorted separately
def merge(A,B):
    # For notational simplicity, I'll assign these to L and R
    L = A
    R = B
    # Return F at the end
    F = []
    while L != [] and R != []:
       # Compare input1 and input2, and put the smallest in the list
       input1 = L[0]
       input2 = R[0]
       if input1 < input2:
          F.append(input1)
          L.pop(0)
       else:
          F.append(input2)
          R.pop(0)
    if L == []:
       if R == []:
          return F
       else:
          for i in R:
             F.append(i)
    if R == []:
       for i in L:
          F.append(i)
    return F

# Test
A = [2,3,4]
B = [1,4,5,6]

print(merge(A,B))

print("**************************************************************************************************************")

print('Insert sort:')


# Now, we implement our insert_sort algorithm

# Let A be an array (list) which we want to sort
def insert_sort(A):
    # This omits the possibility of our list being length 2, so we'll have a special case
    if len(A) == 2:
        if A[1] < A[0]:
            A[0], A[1] = A[1],A[0]
        return A
    for i in range(1, len(A)):
        # Value we're going to sort
        key = A[i]
        # New index
        j = i-1
        # Move the entries up until we reach one which is smaller than what we have
        while j > 0 and A[j] > key:
            A[j+1] = A[j]
            j -=1
        # This is the last point in which we have a value which is larger than our current, and so we set our value.
        A[j+1] = key
    return A

# Test
A = [1,3,2,5,4,1]
print(insert_sort(A))

# Now that we know they both work separately, we combine them for our new merge_sort

print("**************************************************************************************************************")

print('Modified merge sort:')

# k is the number of sub lists that we'll set
def merge_sort(A, k):
    if len(A) > k:
       q = math.floor(len(A)/2)
       X = merge_sort(A[0:q], k)
       Y = merge_sort(A[q:len(A)], k)
       return merge(X,Y)
    else:
       return insert_sort(A)

# Use the decorator to see how long it takes. Because of the recursion, we can't attach the decorator to the last
# function.
@timeit
def time_merge_sort(A,k):
    merge_sort(A,k)

A = random.sample(range(100),90)

# We now test different k's from 2 to 8
for i in range(2, 40):
    time_merge_sort(A,i)

print("**************************************************************************************************************")

print("Bubblesort: ")

# Make the bubblesort algorithm
# Let A be our list, per usual
def bubblesort(A):
    for i in range(len(A)-1):
        j = len(A)-1
        while j >= i+1:
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
            j -=1
    return A

# Test
A = random.sample(range(20), 10)
print(bubblesort(A))




