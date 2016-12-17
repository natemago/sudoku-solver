#!/usr/bin/env python3

from queue import Queue
from collections import namedtuple
from threading import Thread
from random import shuffle, randint


def get_valid_moves(sudoku, x, y, stoh=0):
  used_digits = set()
  # check by row/column
  for i in range(0,9):
    if sudoku[i][x] > 0:
      used_digits.add(sudoku[i][x])
    if sudoku[y][i] > 0:
      used_digits.add(sudoku[y][i])
  
  # check by quadrant
  qx = x//3
  qy = y//3
  for i in range(0, 3):
    for j in range(0, 3):
      if sudoku[qy*3 + i][qx*3 + j] > 0:
        used_digits.add(sudoku[qy*3 + i][qx*3 + j])
  
  valid = [i for i in filter(lambda d: d not in used_digits, [j for j in range(1, 10)])]
  if not len(valid):
    return valid
  if stoh:
    if stoh == 1:
      return [valid[randint(0, len(valid)-1)]]
    shuffle(valid)
    if len(valid) > stoh:
      valid = valid[0:stoh]
  return valid


def next_unsolved_pos(sudoku):
  """Returns next unsolved position, quadrant by quadrant
  """
  for qx in range(0, 3):
    for qy in range(0, 3):
      for x in range(0, 3):
        for y in range(0, 3):
          if sudoku[qy*3+y][qx*3+x] == 0:
            return (qx*3 + x,qy*3 + y)
  return None

def all_unsolved_pos(sudoku):
  for y in range(0, 9):
    for x in range(0,9):
      if sudoku[y][x] == 0:
        yield (x,y)
      
  
def is_solved(sudoku):
  return sum([sum(row) for row in sudoku]) == 405

def clone_with_move(sudoku, x, y, v):
  clone = []
  for i in range(0, 9):
    if i == y:
      clone.append([])
      for j in range(0, 9):
        if j == x:
          clone[i].append(v)
        else:
          clone[i].append(sudoku[i][j])
    else:
      clone.append(sudoku[i])
  return clone

def as_str(sudoku):
  s =  '+---------+---------+---------+\n'
  r = 1
  for row in sudoku:
    s += '|'
    for i in range(0,9):
       s += ' %d ' % row[i]
       if (i+1)%3 == 0:
        s += '|'
    s += '\n'
    if r % 3 == 0:
      s += '+---------+---------+---------+\n'
    r += 1
  return s

def solve(sudoku, find_all=False, par=4, stoh=0, siter=1000):
  """Solves a sudoku from existing sudoku board.
  If the sudoku is an empty board, will try to generate sudoku board (solved).
  A cell of the board is unsolved if it has value of 0.
  
  Params:
    * sudoku - the actual sudoku board to solve
    * find_all - find all solutions. If set to False, it would break after the first solution.
    * stoh - Do a stohastic approach. If set to 0 - the solver is deterministinc and will do
              a BFS (bread-first-search) through the solutions space.
             If set to a value greater than 0, then it will search through at most 'stoh' number
             of possible moves at each stage. Setting it to 1 will cause for the algorithm to
             attempt a pure random solution (it may fail to actually find a solution).
    * siter - valid only if stoh set to some number. Number of times to repeat the random approach
            to find a solution.
  """
  SudokuMove = namedtuple('SudokuMove', ['x', 'y', 'v', 'board'])
 
  stats = {'count': 0, 'solutions': []}
  
  def solve_single_iter():
    """Solves the sudoky.
    If 'stoh' is greater than 0, this would be called 'siter' number of times.
    """
    q = Queue()
    sx, sy = next_unsolved_pos(sudoku)
    for v in get_valid_moves(sudoku, sx, sy, stoh):
        
      q.put(SudokuMove(x=sx, y=sy, v=v, board=clone_with_move(sudoku, sx, sy, v)))
    
    def parallel_solve():
      """This part can be actually split among multpile threads.
      """
      while not q.empty():
        move = q.get()
        
        if is_solved(move.board):
          #print('Solution:')
          #print(as_str(move.board))
          stats['solutions'].append(move.board)
          if not find_all:
            stats['solved'] = True
            break
          continue
        if stats['count'] % 100 == 0:
          stats['state'] = move.board
        
        x,y = next_unsolved_pos(move.board)
        
        for v in get_valid_moves(move.board, x, y, stoh):
          q.put(SudokuMove(x=x, y=y,v=v, board=clone_with_move(move.board, x, y, v)))
        stats['count'] += 1
    
    def peek():
      import time
      while not stats.get('solved'):
        time.sleep(1)
        if stats.get('state'):
          print('%d (%d) - state: \n%s' % (stats['count'], q.qsize(), as_str(stats['state'])))
    
    
    if par:
      threads = [Thread(target=parallel_solve) for i in range(0, par)]
      for t in threads:
        t.start()
      
      pt = Thread(target=peek)
      pt.start()
      
      for t in threads:
        t.join()
      
      stats['solved'] = True
      pt.join()
    else:
      parallel_solve()
  
  if stoh:
    while siter:
      if not find_all and stats.get('solved'):
        break
      solve_single_iter()
      siter -= 1
  
  
  return stats['solutions']


def solve_dfs(sudoku):
  SudokuMove = namedtuple('SudokuMove', ['x', 'y', 'v', 'board'])
  q = []
  solutions_count = 0
  for x,y in all_unsolved_pos(sudoku):
    print ((x,y))
    for v in get_valid_moves(sudoku, x, y):
      q.append(SudokuMove(x=x, y=y, v=v, board=clone_with_move(sudoku, x, y, v)))

    while len(q):
      move = q.pop()
      if is_solved(move.board):
        solutions_count += 1
        print('Solution (%d):' % solutions_count)
        print(as_str(move.board))
        continue
      sx,sy = next_unsolved_pos(move.board)
      V = get_valid_moves(move.board, sx, sy)
      for v in V:
        q.append(SudokuMove(x=sx, y=sy,v=v, board=clone_with_move(move.board, sx, sy, v)))

  print('There are %d solution for this sudoku in total.' % solutions_count)




sudoku = [
  [2,0,0,5,4,0,8,6,0],
  [5,3,4,0,6,0,7,9,0],
  [0,0,8,0,2,9,0,0,4],
  [0,0,3,2,0,0,0,4,0],
  [0,0,0,0,0,0,0,0,0],
  [0,7,0,0,0,6,2,0,0],
  [9,0,0,6,7,0,5,0,0],
  [0,8,5,0,9,0,1,7,6],
  [0,1,6,0,8,5,0,0,9]
]


import sys


if 'dfs' in sys.argv:
  solve_dfs(sudoku)
  sys.exit(0)


if 'gen' in sys.argv:
  sudoku = [[0 for j in range(0,9)] for i in range(0, 9)]
  solutions = solve(sudoku, par=0, stoh=1, siter=5000)
  if len(solutions):
    print(as_str(solutions[0]))
  else:
    print('Failed to generate. Try again for another fun sudoku.')
else:
  print(as_str(sudoku))
  solutions = solve(sudoku, par=0, stoh=1, siter=5000)
  print(' ***** SOLUTIONS *****')
  for solution in solutions:
    print(as_str(solution))
  if not len(solutions):
    print('Unfortunately none has been found. Try running the solver again')
  else:
    print('Found %d solution in total' % len(solutions))