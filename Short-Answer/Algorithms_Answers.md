#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  a = 0
    while (a < n * n * n):
      a = a + n * n

n=1 one operation
n=2 a=5 ,a=9 two operations
n=3 a=15,21,27 three operations.
So for large n the order will be O(n)

b)sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
 - n=1 no of operations=1
   n=2 no of operations=1
   n=3 no of operations=2
   n=4 no of operations= 2
   n=8 no of operations=3
   n=16 no of operations=4
   n=32 no of operations=5

So looks like as n increases the no of opertions follow complexity of O(log2(n))

c) def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
- n=1  no of operations=1
  n=2  no of operations=2
  n=3  no of operations=3

  So the run time compexity of this code is O(n)    

## Exercise II(Egg Problem)

step 0: Start with floor n/2
step 1: Drop an egg from given floor
  - If the egg breaks:
    Increment the counter
    Find the floor at mid point between the ground floor and current floor (round down if necessary)
    If the rounded value is ground floor, then come out of loop
    Go to step 1
  - Else if the egg survives:
    Increment the counter
    Find the floor at mid point between the top floor and current floor (round up if necessary)
    If the rounded value is top floor, then come out of loop
    Go to step 1

I think the complexity would be O(log2(n)).
