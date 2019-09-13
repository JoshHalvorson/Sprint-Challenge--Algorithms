#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n), linear.
This is linear because the while loops end up running n times before meeting the condition


b)
O(n), linear.
The for loop is linear, the bigger n the more operations. The while loop doesnt loop n times since j*=2 will get up to n much faster, making the 
amount of operations pretty small in comparison.


c)
O(n), linear.
Runs n times due to recursive call setting bunnies - 1 each time, which means it will stop when bunnies hits 0. Which ends up being n times

## Exercise II

Get the middle point of floors, check if 'egg breaks', if it does
find a middle point between the current middle and n
find a middle point between the current middle and 0
keep checking if egg is breaking and keep finding the middles if it does
until it doesnt where f will = safe floor

O(logn)
