# CSE200 Python Quiz Prep — Zero to Ready
**Syllabus:** Conditional Statements, Loops, Functions, Lists (1D, 2D)

---

## 1. Conditional Statements (if / elif / else)

Python runs code **only if** a condition is true. Indentation (usually 4 spaces) defines what's "inside" the block — this is not optional in Python, unlike other languages.

```python
age = 20

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

**Key rules:**
- Only ONE branch runs — the first condition that's True.
- `elif` = "else if". You can have zero, one, or many.
- `else` is optional and catches everything else.
- Comparison operators: `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`

```python
x = 7
if x > 0 and x % 2 != 0:
    print("Positive odd number")
```

**Common mistake:** using `=` (assignment) instead of `==` (comparison) inside an `if`. This will actually cause a syntax error in Python, so you'll notice — but double-check anyway.

### Practice
```python
# 1. Write a program that prints "Pass" if marks >= 40, else "Fail"
marks = 35

# 2. Print "Even" or "Odd" for a number n
n = 9

# 3. Given a number, print "Positive", "Negative", or "Zero"
num = -5
```

**Answers:**
```python
# 1
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 2
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

---

## 2. Loops

Loops repeat a block of code. Two types: `for` and `while`.

### `for` loop — when you know how many times / iterating over something

```python
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)
```

**`range()` variations:**
- `range(5)` → 0,1,2,3,4
- `range(2, 6)` → 2,3,4,5
- `range(0, 10, 2)` → 0,2,4,6,8 (step of 2)
- `range(10, 0, -1)` → 10,9,8,...,1 (counting down)

```python
for i in range(1, 6):
    print(i * i)   # prints squares 1 to 25
```

You can also loop directly over a list:
```python
fruits = ["apple", "banana", "mango"]
for f in fruits:
    print(f)
```

### `while` loop — when you don't know exactly how many times, repeat until a condition is false

```python
count = 0
while count < 5:
    print(count)
    count += 1     # CRITICAL: must update the variable or infinite loop!
```

**Danger:** Forgetting to update the loop variable causes an infinite loop. This is the #1 while-loop bug.

### Loop control
- `break` → exits the loop immediately
- `continue` → skips to the next iteration

```python
for i in range(10):
    if i == 5:
        break        # stops entirely at 5
    if i % 2 == 0:
        continue     # skips printing even numbers
    print(i)
```

### Nested loops (loop inside a loop) — very common in exams

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```
Outer loop runs once per iteration of... wait, it's the reverse: for EACH value of `i`, the ENTIRE inner loop runs completely.

**Classic pattern — multiplication table:**
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()   # newline after each row
```
Output:
```
1 2 3
2 4 6
3 6 9
```

### Practice
```python
# 1. Print numbers 1 to 10 using a for loop
# 2. Print the sum of numbers from 1 to 100
# 3. Print all even numbers between 1 and 20 using while
# 4. Print a 5x5 grid of stars using nested loops
```

**Answers:**
```python
# 1
for i in range(1, 11):
    print(i)

# 2
total = 0
for i in range(1, 101):
    total += i
print(total)   # 5050

# 3
n = 1
while n <= 20:
    if n % 2 == 0:
        print(n)
    n += 1

# 4
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
```

---

## 3. Functions

Functions = reusable named blocks of code. Defined with `def`.

```python
def greet(name):
    print("Hello,", name)

greet("Nesar")   # calling the function
```

**Return values** — functions can send a value back using `return`:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8
```

**Key concepts:**
- **Parameters** = variables in the function definition (`a`, `b`)
- **Arguments** = actual values passed when calling (`3`, `5`)
- Once `return` executes, the function stops — code after it won't run
- A function with no `return` returns `None` by default
- **Default parameters**: `def greet(name="friend"):` — lets you call `greet()` with no argument

```python
def power(base, exp=2):
    return base ** exp

print(power(3))       # 9   (uses default exp=2)
print(power(3, 3))    # 27
```

**Scope** (likely to trip you up): a variable created inside a function only exists inside that function.

```python
def my_func():
    x = 10   # local variable
    print(x)

my_func()
print(x)   # ERROR: x is not defined outside the function
```

### Practice
```python
# 1. Write a function is_even(n) that returns True if n is even
# 2. Write a function factorial(n) that returns n!
# 3. Write a function max_of_three(a, b, c) that returns the largest
```

**Answers:**
```python
# 1
def is_even(n):
    return n % 2 == 0

# 2
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 3
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
```

---

## 4. Lists — 1D

A list is an ordered, changeable collection.

```python
nums = [10, 20, 30, 40, 50]
```

**Indexing** (starts at 0!):
```python
print(nums[0])    # 10 (first)
print(nums[-1])   # 50 (last)
print(nums[2])    # 30
```

**Common operations:**
```python
nums.append(60)         # add to end -> [10,20,30,40,50,60]
nums.insert(0, 5)       # insert at index 0
nums.remove(20)         # removes value 20 (first match)
nums.pop()               # removes & returns last element
len(nums)                # length of list
nums[1:3]                # slicing -> elements at index 1,2 (not 3)
sum(nums)                 # sum of all elements
max(nums), min(nums)      # largest/smallest
```

**Looping through a list:**
```python
for x in nums:
    print(x)

# with index:
for i in range(len(nums)):
    print(i, nums[i])
```

**Modifying while looping (needs index):**
```python
for i in range(len(nums)):
    nums[i] = nums[i] * 2
```

### Practice
```python
# 1. Given a list, print the sum of all elements
# 2. Given a list, find and print the maximum value (without using max())
# 3. Given a list, count how many even numbers it contains
```

**Answers:**
```python
data = [4, 8, 15, 16, 23, 42]

# 1
total = 0
for n in data:
    total += n
print(total)

# 2
biggest = data[0]
for n in data:
    if n > biggest:
        biggest = n
print(biggest)

# 3
count = 0
for n in data:
    if n % 2 == 0:
        count += 1
print(count)
```

---

## 5. Lists — 2D (list of lists)

A 2D list is like a grid/matrix — a list where each element is itself a list.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Accessing elements:** `matrix[row][col]`
```python
print(matrix[0][0])   # 1 (row 0, col 0)
print(matrix[1][2])   # 6 (row 1, col 2)
print(matrix[2][1])   # 8 (row 2, col 1)
```

**Looping through a 2D list — ALWAYS nested loops:**

```python
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
```

**Or with indices** (needed when you must know row/col position):
```python
for i in range(len(matrix)):          # rows
    for j in range(len(matrix[i])):    # columns
        print(matrix[i][j], end=" ")
    print()
```

**Building a 2D list from scratch:**
```python
rows, cols = 3, 3
grid = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    grid.append(row)
# grid is now [[0,0,0],[0,0,0],[0,0,0]]
```

### Practice
```python
# 1. Print the sum of ALL elements in a 2D list
# 2. Print the sum of each row separately
# 3. Find the largest element in the 2D list
```

**Answers:**
```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1
total = 0
for row in grid:
    for val in row:
        total += val
print(total)   # 45

# 2
for row in grid:
    row_sum = 0
    for val in row:
        row_sum += val
    print(row_sum)

# 3
largest = grid[0][0]
for row in grid:
    for val in row:
        if val > largest:
            largest = val
print(largest)   # 9
```

---

## Quick Reference Cheat Sheet

| Concept | Syntax |
|---|---|
| If/elif/else | `if x > 0: ... elif x < 0: ... else: ...` |
| For loop | `for i in range(n):` |
| While loop | `while condition:` |
| Break/Continue | `break` exits, `continue` skips |
| Function | `def name(params): return value` |
| List index | `lst[i]` (0-indexed), `lst[-1]` (last) |
| 2D list index | `grid[row][col]` |
| List loop | `for x in lst:` |
| 2D list loop | `for row in grid: for val in row:` |

---

## Mistakes That Cost Marks
1. **Indentation errors** — Python cares about whitespace. Be consistent (use 4 spaces).
2. **Off-by-one errors** — `range(5)` gives 0-4, NOT 1-5.
3. **Forgetting to update loop variables** in `while` → infinite loop.
4. **Confusing `=` and `==`.**
5. **Forgetting `return`** in functions — printing inside a function is not the same as returning a value.
6. **Row/col mixup in 2D lists** — `matrix[row][col]`, not `matrix[col][row]`.

---

## Final Self-Test (do this without looking at answers first)

```python
# 1. Write a function that takes a list and returns True if all numbers are positive
def all_positive(lst):
    # your code

# 2. Print a right triangle pattern of stars, 5 rows:
# *
# **
# ***
# ****
# *****

# 3. Given a 2D list of exam scores (rows = students, cols = subjects),
# write code to print each student's average score.
scores = [[80, 90, 70], [60, 75, 85], [95, 88, 92]]
```

**Answers:**
```python
# 1
def all_positive(lst):
    for n in lst:
        if n <= 0:
            return False
    return True

# 2
for i in range(1, 6):
    print("*" * i)

# 3
for student in scores:
    avg = sum(student) / len(student)
    print(avg)
```
