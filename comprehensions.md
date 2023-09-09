# Comprehensions in Python

Comprehensions provide a nice syntax to extract data from lists. 

There are four types of comprehensions:
* List comprehensions
* Set comprehensions
* Dictionary comprehensions
* Generators


## List comprehensions

List comprehensions allow you to create a list of values from other lists. They are equivalent to a series of map and filter operations, but with nicer syntax.

Let's look at a very simple example:
```python
[ 2*i for i in [1,2,3,4] ]
```
The output is:
```
[2, 4, 6, 8]
```
We iterate over the list `[1, 2, 3, 4]` and for each element we obtain its double `2*i`. Notice for and in are required keywords.


