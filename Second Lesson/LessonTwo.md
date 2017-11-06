# Lesson Two

## Problem 1

Express the function n^3/1000 - 100n^2 - 100n + 3 in terms of big-O notation.

(Sol). Notice that as we take lim_{n -> infty} we have that the function goes to n^3/1000, so it's O(n^3).

## Problem 2

Consider sorting n numbers stored in array A by first finding the smallest element of A and exchaning it with the element in A[1]. Then find the second smallest element of A, and exchange it with A[2]. Continue in this manner for the first n-1 elements of A. Write psuedocode (Python script) for this algorithm, which is known as selection sort. What loop invariant does this algorithm maintain? Why does it need to run for only the first n-1 elements, rather than for all n elements? Give the best-case and worst-case running times of selection sort in big-O notation.

(Sol.) The code is in the Python file. Notice that our loop invariant is broken up into three parts:

### Initialization:

We show it holds for the first loop. Let i = 2, then we have that A[1] is trivially sorted in increasing order.

### Maintenance:

Maintenance: Now assume it hold for i=n-1 and we show it holds for n. Since we have A[1,...,n-2] is sorted in increasing order, we get that the for loop will then go to the n-1th position and see if there are any elements following which are greater. If this does not hold, then we get that it holds for A[1,...,n-1]. If it does hold, then by the for loop we get that it will swap the value so that it holds for A[1,...,n-1]. Hence, it holds.

### Termination: 

It terminates when we have i is greater than the length of A - 1. When this happens, we have i = n+1, where n denotes the length of the list. Substituting this into our maintenance assumption, we get that A[1,...,n] is sorted in increasing order. This, however, means that the list is sorted in increasing order, and so we are done.

## Problem 3

How can we modify almost any algorithm to have a good best-case running time?

(Sol.) On the first iteration, just randomly shuffle the list. Best case, it'll shuffle it in the right order, and then just check to make sure it's increasing. This gives us best-case of O(n) for any algorithm we choose.
