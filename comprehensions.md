# Comprehensions in Python

Comprehensions provide a nice syntax to extract data from lists. 

There are four types of comprehensions:
* List comprehensions
* Set comprehensions
* Dictionary comprehensions
* Generator expressions 


## List comprehensions

List comprehensions allow you to create a list of values from other lists. They are equivalent to a series of map and filter operations, but with nicer syntax.

### Simple example (map)
Let's look at a very simple example:
```python
[ 2*i for i in range(1,5) ]
```
The output is:
```
[2, 4, 6, 8]
```
We iterate over the range `[1, 2, 3, 4]` and for each element we obtain its double `2*i`. Notice `for` and `in` are required keywords. 

#### You try: 

Now, how would you write a comprehension to get each element of a list, multiplied 10 times?

How about each element plus 1?

THINK MORE: How would you do these with a map call?

### if (filter)

Sometimes you don't want to process all the elements of the list. You can process only some elements with the `if` keyword, and adding a predicate (an expression that evaluates to true or false).

For example:
```python
[ 3*i for i in  range(1,11) if i%2==0]
```

Would yield:
```
[6, 12, 18, 24, 30]
```
we're multiplying each element by 3, but only for even elements (if a number is even, its reminder is 0 when you divide it by 2).

#### You try: 

How would you write a comprehension to get each element multiplied by 5, but only odd elements?

### Combining lists (cross-product)

You can also combine elements from two or more lists, and the resulting list would have the cross-product of the elements, similar to a nested for loop. 

```python
[ i+j 
    for i in range(10,60,10) 
    for j in range(1,6)
]
```
Would yield:
```
[11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55]
```
