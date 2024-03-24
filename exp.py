import time


# just the simple recursive exponentiation method with the squaring algorithm
def rec_exp(x, n):
    if n == 0:
        return 1  # return the identity element
    if n == 1:
        return x  # return x if n == 1 because else i would calculate x^0*x^0*x

    k = n // 2  # floor function

    y = rec_exp(x, k)  # calculate x^(n//2)

    # the conquer is different if n is either even or odd
    if n % 2 == 0:
        return y * y
    return y * y * x


# iterative method using the binary representation of the exponent
# x^n can be calculated by accumulating all the powers of x with the exponent
# that is a power of 2, corresponding to bit indexes to 1 in the binary representation of n
def exp(x, n):
    if n == 0:
        return 1  # return the identity element
    y = 1
    while n > 1:
        if (n % 2) != 0:
            y = x * y
            n = n - 1
        x = x * x
        n = n / 2

    return x * y


# iterative method using the binary representation of the exponent
# the binary representation here is calculated before the for loop
def exp2(x, n):

    b = []
    while n > 0:
        b.append(n % 2)
        n = n // 2

    p = 1
    for i in range(len(b)):
        if b[i] == 1:
            p = p * x
        x = x * x

    return p


if __name__ == "__main__":
    res = 99250068772098856700831462057469632637295940819886900519816298881382867104749399077921128661426144638055424236936271872492800352741649902118143819672601569998100120790496759517636465445895625741609866209900500198407153244604778968016963028050310261417615914468729918240685487878617645976939063464357986165711730976399478507649228686341466967167910126653342134942744851463899927487092486610977146112763567101672645953132196481439339873017088140414661271198500333255713096142335151414630651683065518784081203678487703002802082091236603519026256880624499681781387227574035484831271515683123742149095569260463609655977700938844580611931246495166208695540313698140011638027322566252689780838136351828795314272162111222231170901715612355701347552371530013693855379834865667060014643302459100429783653966913783002290784283455628283355470529932956051484477129333881159930212758687602795088579230431661696010232187390436601614145603241902386663442520160735566561

    s = time.time()
    print(rec_exp(123, 456) == res)
    e = time.time()
    print(e - s)

    s = time.time()
    print(exp2(123, 456) == res)
    e = time.time()
    print(e - s)

    s = time.time()
    print(exp(123, 456) == res)
    e = time.time()
    print(e - s)
