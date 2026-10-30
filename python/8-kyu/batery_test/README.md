# Battery Bars

Kata taken from [Codewars](https://www.codewars.com/kata/6ad649de715eb5f5359a7e62).

## Description

Your phone shows its battery as a row of **5 bars**. Each full bar represents **20%** of charge. A bar only lights up when its whole 20% is reached.

Write a function `battery_bars(percent)` that returns the battery as a string:
* `#` for a lit bar
* `.` for an empty bar
* All wrapped in square brackets `[...]`.

---

## Examples

```python
battery_bars(100) # => "[#####]"
battery_bars(70)  # => "[###..]"
battery_bars(20)  # => "[#....]"
battery_bars(19)  # => "[.....]"
battery_bars(0)   # => "[.....]"