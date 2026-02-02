# Python Tutorial --- Data Structures

Based on Python 3 Tutorial --- Data Structures (Chapter 5)

------------------------------------------------------------------------

## 5. Data Structures

This chapter expands on earlier concepts and introduces additional
built‑in data structures in Python.

------------------------------------------------------------------------

## 5.1 More on Lists

### List Methods

``` python
list.append(x)      # add an item to end
list.extend(iter)   # extend by iterable
list.insert(i, x)   # insert at index i
list.remove(x)      # remove first occurrence of x
list.pop([i])       # remove and return item at i (last if omitted)
list.clear()        # remove all items
list.index(x)       # return index of first occurrence
list.count(x)       # count occurrences
list.sort(key=None, reverse=False)  # in-place sort
list.reverse()      # reverse in place
list.copy()         # shallow copy
```

Lists that are modified in place (like `sort()` and `insert()`) return
`None`.

Example:

``` python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')   # 2
fruits.index('banana')  # position of first banana
fruits.sort()
fruits.pop()
```

------------------------------------------------------------------------

### Using Lists as Stacks

``` python
stack = [3, 4, 5]
stack.append(6)
stack.pop()  # returns last element
```

------------------------------------------------------------------------

### Using Lists as Queues

For efficient FIFO queues, use `collections.deque`:

``` python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.popleft()
```

------------------------------------------------------------------------

### List Comprehensions

``` python
squares = [x**2 for x in range(10)]
```

With conditions and multiple loops:

``` python
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

------------------------------------------------------------------------

### Nested List Comprehensions

Matrix transpose example:

``` python
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
transposed = [[row[i] for row in matrix] for i in range(4)]
```

------------------------------------------------------------------------

## 5.2 The `del` Statement

``` python
a = [1,2,3,4]
del a[0]
del a[1:3]
```

`del` can also delete variables entirely.

------------------------------------------------------------------------

## 5.3 Tuples and Sequences

``` python
t = (1, 2, 'hello')
x, y, z = t
```

Tuples are immutable sequences and support unpacking.

------------------------------------------------------------------------

## 5.4 Sets

``` python
basket = {'apple', 'orange', 'banana'}
a = set('abracadabra')
b = set('alacazam')
a - b
```

Sets support union, intersection, and difference operations.

------------------------------------------------------------------------

## 5.5 Dictionaries

``` python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel.get('unknown', None)
```

Dictionary comprehension:

``` python
{x: x**2 for x in (2, 4, 6)}
```

------------------------------------------------------------------------

## 5.6 Looping Techniques

-   `enumerate()` for index and value
-   `zip()` to iterate multiple sequences
-   `reversed()` for reverse order
-   `sorted()` to loop in sorted order

Example:

``` python
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
```

------------------------------------------------------------------------

## 5.7 More on Conditions

-   `in`, `not in` (membership)
-   `is`, `is not` (identity)
-   Chained comparisons: `a < b == c`
-   Boolean operators: `and`, `or`, `not`

------------------------------------------------------------------------

## 5.8 Comparing Sequences

Sequences are compared lexicographically:

-   Compared left to right
-   Shorter sequence is smaller if it is a prefix
-   Nested sequences compare recursively

------------------------------------------------------------------------

End of Document
