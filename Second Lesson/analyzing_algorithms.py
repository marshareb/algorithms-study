# Exercise 2.2-1

# Express the function n^3/1000 - 100n^2 - 100n + 3 in terms of big-O notation
# Clearly the highest order is 3, so we have O(n^3).

# Exercise 2.2-2
# Input: An array A
# Output: Sorted
def selection_sort(A):
    for i in range(len(A)-1):
        index = i
        min = A[i]
        for j in range(i+1, len(A)):
            if A[j] < min:
                min = A[j]
                index = j
        A[index] = A[i]
        A[i] = min
    return A

# Example
A =[5,4,1,2,3]
print(selection_sort(A))

# Loop invariant:
# * Initialization: We show it holds for the first loop. Let i = 2, then we have that A[1] is trivially sorted in
# increasing order.
# * Maintenance: Now assume it hold for i=n-1 and we show it holds for n. Since we have A[1,...,n-2] is sorted in
# increasing order, we get that the for loop will then go to the n-1th position and see if there are any elements
# following which are greater. If this does not hold, then we get that it holds for A[1,...,n-1]. If it does hold, then
# by the for loop we get that it will swap the value so that it holds for A[1,...,n-1]. Hence, it holds.
# * Termination: It terminates when we have i is greater than the length of A - 1. When this happens, we have i = n+1,
# where n denotes the length of the list. Substituting this into our maintenance assumption, we get that A[1,...,n]
# is sorted in increasing order. This, however, means that the list is sorted in increasing order, and so we are done.

# Finally, we do analysis on this to find the big-O value. Notice that with each loop we are looking at less and less
# data, and so we can model this with \sum_{j=1}^{n-1} n - j. Since this is a finite sum, we can break this into parts,
# and so we have \sum_{j=1}^{n-1}n - \sum_{j=1}^{n-1}j. The first sum has nothing indexed, and so this is simply
# n(n-1) - \sum_{j=1}^{n-1}j. Using Gauss's formula for sums, we get n(n-1) - (n)(n-1)/2. We do not need to evaluate
# this; since we see that the highest order must be n^2. Hence, our big-O value is going to be n^2. This is both best
# case and worst case, since regardless we have to iterate through all the corresponding values.

# Exercise 2.2-4

# See markdown.
