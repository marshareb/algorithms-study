import math
# Create the merge function in python.

# A is an array (list)
# p, q, r are indices of A.


def merge(A, p, q, r):
   # We assume that L and R are sorted in this algorithm
   L = A[p:q+1]
   R = A[q+1: r]
   # Sentinel value will be 'x'
   L.append('x')
   R.append('x')
   F = []
   while L != [] and R != []:
      input1 = L[0]
      input2 = R[0]
      if input1 == 'x':
         if input2 == 'x':
            break
         else:
            F.append(input2)
            R.pop(0)
      else:
         if input2 == 'x':
            F.append(input1)
            L.pop(0)
         else:
            if input1 <= input2:
               F.append(input1)
               L.pop(0)
            else:
               F.append(input2)
               R.pop(0)
   return F

# Test input
A = [1,1,1,2,4,5,7,1,2,3,6,1]
print(merge(A,3,6,11))

# Exercise 2.3-1 is an image file in the folder

# Exercise 2.3-2

# Rewrite the merge function so it doesn't use sentinels, but instead stops once the lists are done

def merge(A, p, q, r):
   # We assume that L and R are sorted in this algorithm
   L = A[p:q+1]
   R = A[q+1: r]
   # No sentinel value this time
   F = []
   while L != [] and R != []:
      input1 = L[0]
      input2 = R[0]
      if input1 <= input2:
        F.append(input1)
        L.pop(0)
      else:
        F.append(input2)
        R.pop(0)
   if L == [] and R != []:
       for i in R:
           F.append(i)
   if R == [] and L != []:
       for i in L:
           F.append(i)
   return F

# Test input
A = [1,1,1,2,4,5,7,1,2,3,6,1]
print(merge(A,3,6,11))

# Gives the same thing as before!

# Remaining exercises in markdown