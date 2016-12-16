# sudoku-solver
Sudoku solver and generator for the lulz

# Install
Make sure you have python3 installed.
Then just grab sudoky.py.

# Generate sudoku

To generate a random sudoku, do:

```
python3 sudoku.py gen
```
And you'll have your random sudoku as:
```
+---------+---------+---------+
| 8  3  1 | 3  5  2 | 2  7  1 |
| 6  4  2 | 8  6  4 | 4  8  6 |
| 9  7  5 | 9  1  7 | 9  5  3 |
+---------+---------+---------+
| 5  8  4 | 7  2  1 | 5  4  7 |
| 7  6  9 | 6  4  3 | 3  9  2 |
| 2  1  3 | 5  8  9 | 6  1  8 |
+---------+---------+---------+
| 3  2  7 | 1  9  6 | 1  2  5 |
| 1  9  8 | 4  7  5 | 7  6  4 |
| 4  5  6 | 2  3  8 | 8  3  9 |
+---------+---------+---------+
```


# Solve a sudoku

Runnig the script without params solves a test example (embedded in the code) with a random solution:

```
$ python3 sudoku.py
+---------+---------+---------+
| 2  0  0 | 5  4  0 | 8  6  0 |
| 5  3  4 | 0  6  0 | 7  9  0 |
| 0  0  8 | 0  2  9 | 0  0  4 |
+---------+---------+---------+
| 0  0  3 | 2  0  0 | 0  4  0 |
| 0  0  0 | 0  0  0 | 0  0  0 |
| 0  7  0 | 0  0  6 | 2  0  0 |
+---------+---------+---------+
| 9  0  0 | 6  7  0 | 5  0  0 |
| 0  8  5 | 0  9  0 | 1  7  6 |
| 0  1  6 | 0  8  5 | 0  0  9 |
+---------+---------+---------+

 ***** SOLUTIONS *****
+---------+---------+---------+
| 2  9  7 | 5  4  7 | 8  6  1 |
| 5  3  4 | 3  6  1 | 7  9  2 |
| 1  6  8 | 8  2  9 | 3  5  4 |
+---------+---------+---------+
| 6  5  3 | 2  5  4 | 9  4  5 |
| 8  2  1 | 7  3  8 | 6  1  3 |
| 4  7  9 | 9  1  6 | 2  8  7 |
+---------+---------+---------+
| 9  4  2 | 6  7  2 | 5  3  8 |
| 3  8  5 | 1  9  3 | 1  7  6 |
| 7  1  6 | 4  8  5 | 4  2  9 |
+---------+---------+---------+

Found 1 solution in total

```

I promise to make it read your sudoku boards easily :).
