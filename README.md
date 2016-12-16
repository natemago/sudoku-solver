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
| 7  5  4 | 2  6  3 | 1  9  8 |
| 8  2  1 | 9  4  5 | 7  6  3 |
| 9  3  6 | 8  1  7 | 2  4  5 |
+---------+---------+---------+
| 5  7  2 | 6  8  9 | 4  3  1 |
| 3  1  8 | 7  2  4 | 6  5  9 |
| 4  6  9 | 3  5  1 | 8  2  7 |
+---------+---------+---------+
| 1  9  7 | 4  3  2 | 5  8  6 |
| 2  8  5 | 1  9  6 | 3  7  4 |
| 6  4  3 | 5  7  8 | 9  1  2 |
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
| 2  9  7 | 5  4  3 | 8  6  1 |
| 5  3  4 | 1  6  8 | 7  9  2 |
| 1  6  8 | 7  2  9 | 3  5  4 |
+---------+---------+---------+
| 6  5  3 | 2  1  7 | 9  4  8 |
| 8  2  1 | 9  5  4 | 6  3  7 |
| 4  7  9 | 8  3  6 | 2  1  5 |
+---------+---------+---------+
| 9  4  2 | 6  7  1 | 5  8  3 |
| 3  8  5 | 4  9  2 | 1  7  6 |
| 7  1  6 | 3  8  5 | 4  2  9 |
+---------+---------+---------+

Found 1 solution in total

```

I promise to make it read your sudoku boards easily :).
