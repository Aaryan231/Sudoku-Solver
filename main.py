def print_sudoku(ls):
    print("+" + "---+"*9)
    for i, row in enumerate(ls):
        print(("|" + " {} | {} | {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)


def isEmpty(ls, l):
    for i in range(9):
        for j in range(9):
            if ls[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def isValid(ls, row, col, val):
    a = False
    b = False
    c = False

    for i in range(9):
        if ls[i][col] == val:
            a = True

    for j in range(9):
        if ls[row][j] == val:
            b = True

    row = (row // 3) * 3
    col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if ls[row+i][col+j] == val:
                c = True
    return not a and not b and not c


def Solver(ls):
    l = [0, 0]
    if not isEmpty(ls, l):
        return True

    for k in range(1, 10):
        if isValid(ls, l[0], l[1], k):
            ls[l[0]][l[1]] = k

            if Solver(ls):
                return True

            ls[l[0]][l[1]] = 0

    return False


if __name__ == "__main__":
    ls = [[0 for x in range(9)] for y in range(9)]

    if Solver(ls):
        print_sudoku(ls)
    else:
        print("No Solution Exist!")