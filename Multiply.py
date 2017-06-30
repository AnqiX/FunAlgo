print("Hello World!")
import math

num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

def multiply(x, y):
    m = min(len(str(x)), len(str(y))) - 1

    if m == 0:
        return x * y

    x0 = x % 10 ** m
    x1 = math.floor(x / 10 ** m)

    y0 = y % 10 ** m
    y1 = math.floor(y / 10 ** m)

    z0 = multiply(x0, y0)
    z1 = multiply(x1, y0) + multiply(x0, y1)
    z2 = multiply(x1, y1)

    product = z2 * 10 ** (2 * m) + z1 * 10 **m + z0
    return product

print(multiply(num1, num2))
