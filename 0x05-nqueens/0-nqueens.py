#!/usr/bin/python3
"""
    nqueen problem solution using backtracking, state space tree and bonding solution
"""
import sys

def validate():
    """
        Validates the user input if it is valid (An Integer Greater Than 4)
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    elif not sys.argv[1].isnumeric():
        print("N must be a number")
        sys.exit(1)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    return int(sys.argv[1])

def nqueens():
    """
        Calculates the possible positions for a Queen to avoid attacking by n - 1 Queens
    """
    n_val = validate()
    col = set()
    pos_diag = set() # (r_val + c_val)
    neg_diag = set() # (r_val - c_val)

    fin_res = []
    pos_sol = []

    def backtrack(r_val):
        if r_val == n_val:
            fin_res.append(pos_sol.copy())
            pos_sol.clear()
            return

        for c_val in range(n_val):
            if c_val in col or (r_val + c_val) in pos_diag or (r_val - c_val) in neg_diag:
                continue

            col.add(c_val)
            pos_diag.add(r_val + c_val)
            neg_diag.add(r_val - c_val)
            pos_sol.append([r_val, c_val])

            backtrack(r_val + 1)

            col.remove(c_val)
            pos_diag.remove(r_val + c_val)
            neg_diag.remove(r_val - c_val)
            if pos_sol:
                pos_sol.pop()

    backtrack(0)
    for res in fin_res:
        print(res)


if __name__ == "__main__":
    nqueens()
