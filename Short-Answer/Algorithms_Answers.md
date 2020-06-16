#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I



a)  a = 0
    while (a < n * n * n):
      a = a + n * n

 O(n) , linear for large n

b)
sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

n=4 no of operations= 2
n=8 no of operations=3
n=16 no of operations=4
n=32 no of operations=5

Logarithmic  O(log n)

c) def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

n=1  no of operations=1
n=2  no of operations=2
n=3  no of operations=3
Runtime Complexity : Linear O(n)

   Space complexity : O(n)


## Exercise II
The best approach is to use binary search for this algorithm .
Start with floor n/2
Then drop an egg from given floor(n/2)
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

Time complexity would be O(log2(n)).
