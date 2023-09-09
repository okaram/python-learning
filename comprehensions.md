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

#### you try 

Now, how would you write a comprehension to get each element of a list, multiplied 10 times?

How about each element plus 1?

THINK MORE: How would you do these with a map call?

### if / filter

Sometimes you don't want to process all the elements of the list.

