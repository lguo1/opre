import time
import numpy as np
import math
from itertools import combinations

def queen_moves(r,c,board,n):
    board[r,:] = 0
    board[:,c] = 0
    diff = r-c
    if diff > 0:
        board[(range(diff,n), range(0,n-diff))] = 0
    else:
        board[(range(0,n+diff),range(-diff,n))] = 0
    upright = range(max(r+c+1-n,0), min(r+c+1,n))
    board[(list(reversed(upright)), upright)] = 0

def main():
    n = 4
    max = 0
    board = np.ones((n,n))
    unique = []
    for i in range(math.ceil(n/2)+1):
        for j in range(i+1):
            unique.append((i,j))

    rest = []
    for i in range(n):
        for j in range(n):
            if (i,j) not in unique:
                rest.append((i,j))
                
    for comb in combinations(pos,n):
        for q in comb:
            queen_moves(*q, board, n)
        current = np.sum(board)
        board[:] = 1
        if current > max:
            optimal = comb
            max = current
    print(optimal)
    print(max)

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
