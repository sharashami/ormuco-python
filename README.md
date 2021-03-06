# ormuco-python

# Question A:
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

## Approach:
* I walked through the problem following PEDAC. One can see my notes in approach folder
* Having my notes in mind, I started coding following TDD approach using the built-in unit test library
* The question asked for a 'program', I understood like putting the code out of a function. One can see such approach in main.py file. I built it as command line program. On the other hand, I thought it would be better having this as a module, so I created a module called 'lines' with a function called 'overlap'. On can check it in main_from_module.py
* I used docstring to write the documentation for it.

### Overall, some main rules considered:
* A line cannot have the same start and end value
* The start and end value must be different so it represents a line segment
* The input can be positive/negative float values
* Two lines overlap if at least one end of the line is between the other line's ends. If the lines share the same end it is considered as overlapping as well

# Question B:
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

## Approach
* I walked through the problem following PEDAC. One can see my notes in approach folder
* Having my notes in mind, I started coding following TDD approach using the built-in unit test library
* I understood that you want me to create an independent function responsible for doing what the question asked. Thus, I came up with stringutils module that you can add to any other function related to strings you want and start using them. Moreover, you can start using stringutils in any project right away. 
* I used docstring to write the documentation for it.
* When I saw the question description I remembered of comparing characters with C Language, so I tackled the question using the same approach: Ascii character table.

## Overall, some main rules considered:
 
* Every input is treated as a string.
* The function returns -1 if str1 is less than str2, 0 if equal, and 1 if greater than. 
* The solution is case-sensitive since ascii table assigns different values to 'a' and 'A', for example.

## Want start using it?

```
import stringutils
stringutils.compare('really','straightforward')
```

## Wanna know what stringutils has to offer?

```
import stringutils
help(stringutils)
```

# Runing the tests
```
$ python -m unittest test_something.py
```
or
```
$ python test_something.py
```