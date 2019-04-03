# ormuco-python

# Question A:
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

## Approach:
* I walked through the problem following PEDAC. One can see my notes in approach folder
* Having my notes in mind, I started coding following TDD approach using the built-in unit test library

### Overall, some main rules considered:
* A line cannot have the same start and end value
* The start and end value must be different so it represents a line segment
* The input can be positive/negative float values
* Two lines overlap if at least one end of the line is between the other line's ends. If the lines share the same end it is considered as overlapping as well

# Question B:
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

# Runing the tests
```
$ python -m unittest test_something.py
```
or
```
$ python test_something.py
```