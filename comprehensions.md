# Comprehensions in Python

Comprehensions provide a nice syntax to extract data from lists. 

There are four types of comprehensions:
* List comprehensions
* Set comprehensions
* Dictionary comprehensions
* Generators


## List comprehensions

List comprehensions allow you to create a list of values from other lists. They are equivalent to a series of map and filter operation, but with nicer syntax.

Let's look at a very simple example:
```python
[ 2*i for in in [1,2,3,4] ]
```
