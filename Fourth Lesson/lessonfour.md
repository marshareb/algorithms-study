#Fourth Lesson

## Problem 1 (Insertion Sort on Small Arrays in Merge Sort)

Although merge sort runs in O(n lg(n)) worst-case time and insertion sort runs in O(n^2) worst-case time, the constant factors in insertion sort can make it faster in practice for small problem sizes on many machines. Thus, it makes sense to coarsen the leaves of the recursion by using insertion sort within merge sort when subproblems become sufficiently small. Consider a modification to merge sort in which n/k sublists of length k are sorted using insertion sort and then merged using the standard merging mechanism, where k is a value to be determined.

(a.) Show that insertion sort can sort the n/k sublists, each of length k, in O(nk) worst-case time.

(b.) Show how to merge the sublists in O(n lg(n/k)) worst-case time.

(c.) Given that the modified algorithm runs in O(nk + nlg(n/k)) worst-case time, what is the largest value of k as a function of n for which the modified algorithm has the same running time as standard merge sort, in terms of O-notation?

(d.) How should we choose k in practice?

(Sol.) (a.) From the problem explanation, we recall that insertion sort runs in O(n^2). Hence, with a sublist of size k, we get O(k^2). Hence, our worst case is going to be O((n/k)*k^2) = O(nk).

(b.) The size of our lists is going to be lg(n)-lg(k) = lg(n/k). The merge algorithm will run the same, and so we get O(nlg(n/k)).

(c.) Assume that k(n) is in O(lg(n)). Then we have O(n(k+lg(n/k)) = O(n(lg(n) + lg(n/lg(n))) = O(n(lg(n))) by basic log rules, which is the same as merge sort. Hence, so long as we have that k(n) is in O(lg(n)) as a function of n, we have that it will have the same running time as the standard merge sort.

(d.) In theory, we could try to minimize the prior equation. In practice, I would just try values within a range and see how it goes.

## Problem 2

Try to implement the problem before in Python, and test different values of k and see how long they take.

(Sol.) Repeated applications on randomly genereated lists of size 90 sees that around k=37 is a good value.

## Problem 3 (Correctness of Bubblesort)

Bubblesort is a popular, but inefficient sorting algorithm. It works by repeatedly swapping adjacent elements that are out of order.

(a.) Write the bubblesort algorithm in Python.

(b.) Let A' denote the output of Bubblesort(A). To prove that Bubblesort is correct, we need to prove that it terminates and A'[1] <= A'[2] <= ... <= A'[n], where n = A.length. In order to show that Bubblesort actually sorts, what else do we need to prove?

(c.) State precisely a loop invariant for the for loop in lines 2-4, and prove that this loop invariant holds. Your proof should use the structure of the loop invariant proof presented in this chapter.

(d.) Using the termination condition of the loop invariant proven in part (c.), state a loop invariant for the for loop in lines 1-4 that will allow you to prove the inequality. Your proof should use the structure of the loop invariant proof presented in this chapter.

(e.) What is the worst-case running time of bubblesort? How does it compare to the running time of insertion sort?

(Sol.) (a.) See Python code.

(b.) I'm guessing that A' has the same elements as A, although this seems quite obvious by how we defined Bubblesort (it only swaps values of A).

(c.)  The loop invariant has three properties to consider:

### Initialization

We see that at the first loop, we have that the position of the smallest element could be anywhere, and in particular the maximum index is at the end of the list, which is the length. 

### Maintenance

Assume we know it holds for j. Then we have that the smallest element of A[i..j] could be A[j]. Examining A[j], if A[j] < A[j-1], we swap the elements so that A[j-1] < A[j]. Hence, we now have that the smallest element is in the range A[i..j-1] could be A[j-1]. If it is the case that A[j] >= A[j-1], then we lose no information by doing nothing, and so the smallest element could still be in the range A[i..j-1]. So maintenance holds.

### Termination

Finally, we know that when the algorithm terminates the smallest element of A[i..j] will be at the A[i] position. 

(d.) Again, we consider the three properties:

### Initialization

Before the first loop, we have that A[1] is clearly sorted, and so we're done.

### Maintenance

We now assume it holds for n, that is, A[1..n] is sorted. We then look at the next element, A[n+1]. By the prior loop invariant, we have that A[n+1] will be the smallest element in the list A[n+1...A.length] so that A[1..n+1] will be sorted. Hence, it holds for the next iteration.

### Termination

We see that when this terminates we have that the list will be sorted.

(e.) Both in the best and worst case, we see that we will iterate over all of the elements twice, giving us O(n^2). This is the same worst-case running time, but it has a worse best-case running time, since insertion sort could run in O(n).

## Problem 4

This is the correctness of Horner's rule.

In terms of O-notation, what is the running time of this code fragment for Horner's rule?

(Sol.) It's O(n), because we iterate through all of the n elements once.















