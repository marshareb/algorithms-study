# Lesson Three

## Problem 1

Convert the merge algorithm to Python.

(Sol.) Code is in the Python file.

## Problem 2

Using Figure 2.4 as a model, illustrate the operation of merge sort on the array A = [3,41,45,26,38,57,9,49]

(Sol.) ![alt text](https://i.imgur.com/oINtQ8D.jpg)

## Problem 3

Rewrite the Merge procedure so that it does not use sentinels, instead stopping once either array L or R has had all its elements copied back to A and then copying the remainder of the other array back into A.

(Sol.) Code is in the Python file.

### Remark

I'm going to be using pseudo-latex for the next problem.

## Problem 4

Use mathematical induction to show that when n is an exact power of 2, the solution of the recurrence $T(n) = \{ 2 \quad \text{ if }n=2, 2T(n/2)+n \quad \text{ if } n=2^k \text{, for k > 1} \}$ is $T(n) = n\log(n)$ (here, $\log$ stands for $\log_2$).

(Sol.) For the base case, let $n =2$. Then we have $T(2) = 2\log(2) = 2$, as required. Next, assume it holds for $2^{k-1}$ and we show it holds for $2^k$. Notice we have $T(2^k) = 2 * T(2^{k-1}) + 2^k$. By the induction hypothesis, it holds for $2^{k-1}$, and so we have $2 * (2^{k-1} \log(2^{k-1})) + 2^k = 2^k \log(2^{k-1}) + 2^k = 2^k(\log(2^{k-1}) + 1) = 2^k (k) = 2^k \log(2^k)$ as required. 

## Problem 5

We can express insertion sort as a recursive procedure as follows. In order to sort A[1..n], we recursively sort A[1..n-1] and then insert A[n] into the sorted array A[1..n-1]. Write a recurrence for the running time of this recursive version of insertion sort.

(Sol.) If there is only one element, we get that we just need to insert our element into our array and so we get O(1) for the run time. If there is more than one element, we recursively add our running time minus one element to the time it takes to run the insert algorithm on the n elements. This can be written as T(n-1) + O(n), where T(n-1) denotes the run time for the n-1th element. Hence, we get $T(n) = \{ O(1) \text{ if } n=1, \quad T(n-1) + O(n) \text{ if } n>1\}$.
