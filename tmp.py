import numpy as np
from scipy.fft import fft

def diocane(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [0.0] * (N // 2)
    for k in range(N // 2):
        T[k] = np.exp(-2j * np.pi * k / N) * odd[k]
    return np.array(
        [even[k] + T[k] for k in range(N // 2)]
        + [even[k] - T[k] for k in range(N // 2)]
    )

def my_fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = my_fft(x[0::2])
    odd = my_fft(x[1::2])
    T = [0.0] * (N // 2)
    for k in range(N // 2):
        T[k] = np.exp(-2j * np.pi * k / N) * odd[k]
    return np.array(
        [even[k] + T[k] for k in range(N // 2)]
        + [even[k] - T[k] for k in range(N // 2)]
    )

def my_ifft(x):
    n = len(x)
    a = my_fft(x)
    i = 0
    while i < n:
        a[i] = a[i] / n
        i += 1
    return a

if __name__ == "__main__":
    # print(poly_mul(np.array([0, 2, 1, 4]), np.array([1, 4, 3, 2])))
    # print(my_poly_mul(np.array([0, 2, 1, 4]), np.array([1, 4, 3, 2])))

    # y = np.array([0, 2, 1, 4])
    x = np.array([1,4,3,2])
    # # tmp(x)
    print(fft(x))
    print(my_fft(x))
    # print()
    # print(np.abs(ifft(x)))
    # print(np.abs(my_ifft(x)))
    # print(np.abs(ifft(x)) == np.abs(my_ifft(x)))
    # print()

    # print(ifft(x))
    # print(np.ifft(x))
    # print(my_ifft(x))

    # tmp = [0] * len(x)
    # n = len(x)
    # a = fft(x)
    # tmp[0] = 1/n * a[0]
    # i = 1
    # while i < n:
    #     tmp[i] = 1/n * a[n-1]
    #     i += 1
    # print(np.array(tmp))

    # tmp = [0] * len(x)
    # n = len(x)
    # a = my_fft(x)
    # tmp[0] = 1/n * a[0]
    # i = 1
    # while i < n:
    #     tmp[i] = 1/n * a[n-1]
    #     i += 1
    # print(np.array(tmp))

    # a1, b1, c1 = poly_mul(np.array([0,2,1,4]), np.array([1,4,3,2]))
    # a2, b2, c2 = my_poly_mul(np.array([0,2,1,4]), np.array([1,4,3,2]))
    # print("A1")
    # print(a1)
    # print("A2")
    # print(a2)
    # print("B1")
    # print(b1)
    # print("B2")
    # print(b2)
    # print("C1")
    # print(c1)
    # print("C2")
    # print(c2)

