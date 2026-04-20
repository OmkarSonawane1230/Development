N = 4
board = [-1]*N

def safe(r, c):
    for i in range(r):
        if board[i] == c or abs(board[i]-c) == r-i:
            return False
    return True

def print_board():
    for r in range(N):
        for c in range(N):
            print("Q" if board[r]==c else ".", end=" ")
        print()
    print()
#
def solve(r):
    if r == N:
        print_board()
        return True
    for c in range(N):
        if safe(r, c):
            board[r] = c
            if solve(r+1):
                return True


# FIX FIRST QUEEN HERE
board[0] = 2  # fixes queen at row 0, column 2
solve(1) # start solving from row 1