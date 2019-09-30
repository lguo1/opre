import numpy as np
import math
from itertools import combinations
from progress.bar import Bar

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

def place_queens(n, max):
    board = np.ones((n,n))
    unique = []
    rest = []
    bound = math.ceil(n/2)
    optimal = []

    for r in range(n):
        for c in range(n):
            if r <= bound and c <= r:
                unique.append((r,c))
            else:
                rest.append((r,c))

    total = math.factorial(n**2)*len(unique)/math.factorial(n**2-n+1)/math.factorial(n-1)
    bar = Bar('Processing', max=total)
    for i in range(len(unique)):
        first = unique[i]
        for later in combinations(rest+unique[:i]+unique[i+1:],n-1):
            queen_moves(*first, board, n)
            for queen in later:
                queen_moves(*queen, board, n)
            current = np.sum(board)
            bar.next()
            board[:]=1
            if current == max:
                optimal.append([first,*later])
    bar.finish()
    return optimal

def queen_place(r,c,board):
    board[r,c]=0

def display(n, placements):
    for place in placements:
        board = np.ones((n,n))
        for i in range(n):
            queen_place(*place[i],board)
        print(board)
        print()

def main():
    n = 4
    max = 1
    placements = place_queens(n,max)
    print(len(placements))
    display(n,placements)

main()
