found = False
def nQueens(k, n):
    global found
    if found:
        return
    for i in range(1, n + 1):
        if place(k, i):
            x[k] = i
            if k == n:
                found = True
                print("The Positions are : ", end="")
                for i in range(1, len(x)):
                    print(x[i], end=" ")
                print()
                for j in range(1, n + 1):
                    for l in range(1, n + 1):
                        if x[j] == l:
                            print("Q", end=" ")
                        else:
                            print("-", end=" ")
                    print()
            else:
                nQueens(k + 1, n)
def place(k, i):
    for j in range(1, k):
        if x[j] == i or abs(x[j] - i) == abs(j - k):
            return False
    return True
n = int(input("Enter the number of Queens: "))
x = []
if n == 2 or n == 3:
    print("Not Possible")
else:
    x = [0] * (n + 1)
    nQueens(1, n)