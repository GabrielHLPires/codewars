## 📝 Solution: Beginner Series #3 Sum of Numbers (Codewars)

This repository contains my Python solution for the [Beginner Series #3 Sum of Numbers](https://www.codewars.com/kata/55f2b110f61eb01779000053) kata on Codewars.

### 🧠 Problem Description
Given two integers `a` and `b`, which can be positive or negative, find the sum of all the integers between them (inclusive) and return it. If the two numbers are equal, return `a` or `b`.

*Note:* `a` and `b` are not necessarily ordered (i.e., `a` might be greater than `b`).

### 💻 Implementation (Python)

```python
def get_sum(a, b):
    if a > b:
        return sum(range(a, b - 1, -1))
    else:
        return sum(range(a, b + 1))