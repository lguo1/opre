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
    rest = []
    bound = math.ceil(n/2)
    for r in range(n):
        for c in range(n):
            if r <= bound and c <= r:
                unique.append((r,c))
            else:
                rest.append((r,c))
    for i in range(len(unique)):
        first = unique[i]
        for later in combinations(rest+unique[:i]+unique[i+1:],n-1):
            queen_moves(*first, board, n)
            for q in later:
                queen_moves(*q, board, n)
            current = np.sum(board)
            board[:] = 1
            if current > max:
                optimal = first+later
                max = current
    print(optimal)
    print(max)

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
