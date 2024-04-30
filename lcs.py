import numpy as np


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def lcs(X, Y):
    m = len(X) + 1
    n = len(Y) + 1

    # additional cost
    l = np.zeros(([m, n]))
    # additional information
    b = np.zeros(([m, n]), dtype=object)

    for i in range(1, m):
        for j in range(1, n):
            # print("comparing X[" + str(i - 1) + "] to Y[" + str(j - 1) + "]")
            if X[i - 1] == Y[j - 1]:
                l[i, j] = 1 + l[i - 1, j - 1]
                b[i, j] = "NW"
            elif l[i - 1, j] >= l[i, j - 1]:
                l[i, j] = l[i - 1, j]
                b[i, j] = "N"
            else:
                l[i, j] = l[i, j - 1]
                b[i, j] = "W"

    print("ADDITIONAL COST TABLE")
    print(l)
    print("ADDITIONAL INFORMATION TABLE")
    print(b)
    return (l[m - 1, n - 1], b)


def print_lcs(X, b, i, j):
    if (i == 0) or (j == 0):
        return
    if b[i, j] == "NW":
        print_lcs(X, b, i - 1, j - 1)  # vai al carattere precedente prima della stampa
        print(bcolors.OKGREEN + X[i - 1] + bcolors.ENDC)
    elif b[i, j] == "W":
        print_lcs(X, b, i, j - 1)
    else:
        print_lcs(X, b, i - 1, j)


if __name__ == "__main__":
    # LCS: GTAB, with length 4
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    print("calculating the LCS between " + S1 + " and " + S2)
    llast, b = lcs(S1, S2)

    print_lcs(S1, b, len(S1), len(S2))
