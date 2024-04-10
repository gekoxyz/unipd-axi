import cmath
import numpy as np
from scipy.fft import fft, ifft

# evaluate a polinomyal of vector a in z (z is a complex number)
def evaluate(a, z):
    n = len(a)
    y = a[0]
    pow = 1
    for i in range(1, n):
        pow = pow * z
        y = y + a[i] * pow
    return y


# evaluate a polinomyal of vector a in z (z is a complex number)
# the horner algorithm is based on the observation that the expression which
# describes a polinomyal can be described as:
# p(x) = \sum_{i=0}^{n-1} a_i * x_i = a_0 + x(a_1 + x(a_2 + ... + x(a_{n-1})))
def horner_evaluation(a, z):
    n = len(a)
    y = a[n - 1]
    i = 2
    while i <= n:
        y = a[n - i] + z * y
        i += 1
    return y


def my_fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = my_fft(x[0::2])
    odd = my_fft(x[1::2])
    T = [0.0] * (N // 2)
    for k in range(N // 2):
        T[k] = cmath.exp(-2j * cmath.pi * k / N) * odd[k]
    return np.array([even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)])

def my_ifft(x):
    n = len(x)
    a = np.round(my_fft(x), decimals=8)
    tmp = [0] * n 
    tmp[0] = 1/n * a[0]
    i = 1
    while i < n:
        tmp[i] = 1/n * a[n-i]
        i += 1
    return np.array(tmp)

def my_poly_mul(p1, p2):
    deg1 = p1.shape[0] - 1
    deg2 = p2.shape[0] - 1
    # whould be 2*(deg1 + deg2) + 1 but the next_power_of_2 handles the + 1
    total_num_pts = 2 * (deg1 + deg2)
    # this sets the most significant bits to 1 and the other bits to 0
    next_power_of_2 = 1 << (total_num_pts - 1).bit_length()

    # the second argument of np.pad is the number of values padded to the edges of each axis
    ff_p1 = my_fft(np.pad(p1, (0, next_power_of_2 - p1.shape[0])))
    ff_p2 = my_fft(np.pad(p2, (0, next_power_of_2 - p2.shape[0])))
    product = ff_p1 * ff_p2
    inverted = my_ifft(product)
    rounded = np.round(np.abs(inverted)).astype(np.int32)
    return np.trim_zeros(rounded, trim="b")

if __name__ == "__main__":
    x = np.array([0.0, 2.0, 1.0, 4.0])
    
    print("fft")
    print(fft(x))
    print(my_fft(x))
    print()
    print("ifft")
    print(ifft(fft(x)))
    print(my_ifft(my_fft(x)))
    print()
    print("poly mul")
    print(poly_mul(np.array([0,2,1,4]), np.array([1,4,3,2])))
    print(my_poly_mul(np.array([0,2,1,4]), np.array([1,4,3,2])))


