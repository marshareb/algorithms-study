# A is a list of integers
def insert_sort(Ac):
    # Creates a copy since Python will edit the original list otherwise.
    A = [i for i in Ac]
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j > -1 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

# Exercise 2.1-1
A = [31,41,59,26,41,58]
print(insert_sort(A))

# Exercise 2.1-2
def reverse_insert_sort(A):
    return insert_sort(A)[::-1]
print(reverse_insert_sort(A))

# Exercise 2.1-3
# Input: A is a list [a1,...,an] and value is some value in the list
def search(A, val):
    for i in range(len(A)):
        if A[i] == val:
            return i

