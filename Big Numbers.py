
# Just returns a large number you wrote
def method_1():
    return 9999999999999999999999999999


# Returns 9^9^9^9^etc as many as you wrote
def method_2():
    return pow(pow(pow(pow(pow(9, 9), 9), 9), 9), 9)


# Returns 9^i based on a loop
def method_3():
    x = 9
    for i in range(999999999999):
        x = pow(9,x)


# Loops of Loops
def method_4(x, n=2):
    if n > 1:
        x = method_4(n-1, x)
    y = 9
    for i in range(x):
        y = pow(y, y)
    return y


# Loops of Loops of Loops of etc aka Fast growing Hierarchy
def method_5(i, x):
    if i == 0:
        return x + 1
    else:
        y = x
        for i in range(x):
            y = method_5(i-1, y)
        return y


# Fast Growing Hierarchy Diagonalization aka F[Omega]
def method_6(x):
    return method_5(x, x)


# F[Omega] Diagonalization aka F[Omega * i + j] aka F[Omega^2]
def method_7(i, j, x):
    if i == 0 and j == 0:
        return x + 1
    elif j == 0:
        return method_7(i-1, x, x)
    else:
        y = x
        for i in range(x):
            y = method_7(i, j-1, y)
        return y


# F[Omega ^ Omega]
def method_8(n):
    pass # Need to make this one


# A look at the Goodstein Sequence (aka we count the steps in a Fast growing Hierarchy
#
# Example 1
# b^b - Base:3                   || F[Omega](3)
# = b^3 = b^2 + b^2 + b^2        || F[3](3) = F[2](F[2](F[2](3)))
#
# Example 2
# b^(b^b + b) + b^1              || F[Omega^Omega+Omega](F[1](b))
#
# This means that example 2 grows faster than the best function we made above...
# 4 = 2^2, so G(4) = F[Omega](3) - 2 aka 3 * 2^402653211
# 21 = 2^2^2, so G(21) = F[Omega^Omega](F[Omega](F[0](3))) - 2
# aka F[Omega^Omega](F[Omega](4))
# aka F[Omega^Omega](N) where N is basically Infinity

# This means Goodstein is similar to the height of power towers of Omega in the F[]
# Another name for F[Omega^Omega^Omega^etc...] of height Omega is Epsilon[0]
# aka Goodstein grows at F[Epsilon[0]]





