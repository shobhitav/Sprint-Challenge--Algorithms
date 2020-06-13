#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

b) O(log n)

c) O(n)
   Space complexity : O(n)


## Exercise II
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
