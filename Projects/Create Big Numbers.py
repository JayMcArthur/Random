# Just returns a large number you wrote
# F[0]
# 2 + n
def method_1(n):
    return n + 9999999999999999999999999999


# F[1]
# 2n

# F[2]
# 2^n


# Returns 9^9^9^9^etc as many as you wrote, Arrow Notation Base
def method_2():
    return pow(pow(pow(pow(pow(9, 9), 9), 9), 9), 9)


# Returns 9^i based on a loop, Arrow Notation - 2 Arrows
# F[3]
def method_3(n):
    x = 9
    for i in range(n):
        x = pow(9, x)


# Loops of Loops, Arrow Notation - 3 Arrows
# F[4]
def method_4(x, n=2):
    if n > 1:
        x = method_4(n - 1, x)
    y = 9
    for i in range(x):
        y = pow(y, y)
    return y


# Loops of loops of loops of ... aka Fast growing Hierarchy
# F[m]
def method_5(i, x):
    if i == 0:
        return x + 1
    else:
        y = x
        for i in range(x):
            y = method_5(i - 1, y)
        return y


# Fast Growing Hierarchy Diagonalization
# F[ω]
def method_6(x):
    return method_5(x, x)


# F[ω+n]
# NOTES: F[ω+3](3) -> F[ω+2](F[ω+2](F[ω+2](3)))

# F[ω2]
# NOTES: F[ω2](3) -> F[ω+ω](3) -> F[ω+3](3)


# F[ω] Diagonalization aka F[ω · i + j]
# F[ω^2]
def method_7(i, j, x):
    if i == 0 and j == 0:
        return x + 1
    elif j == 0:
        return method_7(i - 1, x, x)
    else:
        y = x
        for i in range(x):
            y = method_7(i, j - 1, y)
        return y


# F[ω^3]
# NOTES: F[ω^3](3) -> F[ω^2 · ω](3) -> F[ω^2 · n](3) -> F[ω^2 · 3](3)
# F[ω^2 · 3](3) -> F[ω^2 + ω^2 + ω^2](3) -> F[ω^2·2 + ω · 3](3) -> F(ω^2 · 2 + ω·2 + 3](3)


# F[ω ^ ω]
class peterC:
    def __init__(self):
        #  This is based off pete-7.c which is F[ω ^ ω](2↑↑35) and F[ω ^ ω](2↑↑36)
        self.F = '(9<<(9<<(9<<(9<<'
        self.D = self.F + self.F + self.F + self.F
        self.E = ')))))))))))))))'
        self.N = self.D + self.D + '99' + self.E + self.E
        self.A = [self.N] * self.N
        self.B = self.N
        self.method_8(self.A)

    def method_8(self, n):
        C = self.B
        b = [None] * self.N
        n = self.N

        n -= 1
        while n:
            b[n] = self.A[n]
            n -= 1
        n = self.N - 1
        b[n] -= 1
        if b[n] > 0:
            C -= 1
            while C:
                B = self.method_8(b)
                C -= 1
        n -= 1
        b[n] -= 1
        while n and not (b[n + 1] == B, b[n]):
            n -= 1
            b[n] -= 1
        return B * B if n == -1 else self.method_8(b)


# F[ε₀]
# F[ε₀](n) = F[ω^ω^...](n) with n - 1 as the height
class methodNine:
    # Based off of Marxen.c aka F[ε₀+ω2](1,000,000)
    def __init__(self, n):
        print(self.h(self.g(9), 9))

    def P(self, x, y):
        if x + y == 0: return 0
        return x % 2 + y % 2 * 2 + 4 * self.P(x / 2, y / 2)

    def H(self, z):
        if z == 0: return 0
        return z % 2 + 2 * self.H(z / 4)

    def I(self, f, e, r):
        if f == 0: return r
        return self.P(self.P(f, e), r)

    def M(self, x, e):
        if x == 0: return 0
        return self.I(x % 2, self.M(e, 0), self.M(x / 2, e + 1))

    def D(self, x, b):
        if x == 0: return 0
        return self.E(self.H(self.H(x)), self.H(self.H(x) / 2), b)

    def E(self, f, e, r, b):
        if e == 0: return self.I(f - 1, e, r)
        return self.E(1, self.D(e, b), self.I(b - 1, self.D(e, b), self.I(f - 1, e, r)), b)

    def F(self, x, b):
        if x == 0: return b
        return self.F(self.D(x, b + 1), b + 1)

    def G(self, x):
        return self.F(self.M(x, 9), 9)

    def f(self, n, x):
        if n == 0: return self.G(x)
        elif x == 0: return self.f(n - 1, self.G(n))
        else: self.f(n - 1, self.G(self.f(n, x - 1)))

    def g(self, x):
        return self.f(x, x)

    def h(self, n, x):
        if n == 0: return self.g(x)
        elif x == 0: return self.h(n - 1, self.g(n))
        else: return self.h(n - 1, self.g(self.h(n, x - 1)))
    # Also Below, Tetrational Level BEAF,
# A look at the Goodstein Sequence (aka we count the steps in a Fast growing Hierarchy
#
# Example 1
# b^b - Base:3                   || F[ω](3)
# = b^3 = b^2 + b^2 + b^2        || F[3](3) = F[2](F[2](F[2](3)))
#
# Example 2
# b^(b^b + b) + b^1              || F[ω^ω+ω](F[1](b))
#
# This means that example 2 grows faster than the best function we made above...
# 4 = 2^2, so G(4) = F[ω](3) - 2 aka 3 · 2^402653211
# 21 = 2^2^2, so G(21) = F[ω^ω](F[ω](F[0](3))) - 2
# aka F[ω^ω](F[ω](4))
# aka F[ω^ω](N) where N is basically Infinity
# This means Goodstein is similar to the height of power towers of ω in the F[]
# Another name for F[ω^ω^ω^etc...] of height ω is ε₀
# aka Goodstein grows at F[ε₀]

# F[ε₀ + n]

# F[ε₀ · n]

# F[ε₀ · ω] -> F[ω^ε₀ · ω] -> F[ω^(ε₀+1)]

# ω^(ε₀·n)
# ω^(ε₀·2) = ω^(ε₀+ε₀) = ω^(ε₀) · ω^(ε₀) = (ω^ε₀)^2 = ε₀^2 = ε₀·ε₀

# ω^ε₀·ω = ε₀·ε₀·...ε₀·ε₀

# F[ε₁]
# NOTES: F[ε₁] = F[ω^ω^ω^ω^...ω^(ε₀ + 1)] = F[ε₀^ε₀^...ε₀]
# PROOF:  ω^...ω^(ε₀ + 1) = ε₀^...ε₀
# ------ Note - ω^...ω^(ε₀ + 1) = ω^...ω^(ε₀·2) due to increasing "2" to ω just adds ω to the stack
# ------ ω^ω^(ε₀·2) = ω^(ω^ε₀)^2 = ω^ε₀^2 = ω^(ε₀·ε₀) = (ω^ε₀)^ε₀ = ε₀^ε₀
# ------ ω^ω^ω^(ε₀·2) = ω^ε₀^ε₀ = ω^ε₀^(1+ε₀) = ω^(ε₀·ε₀^ε₀) = (ω^ε₀)^ε₀^ε₀ = ε₀^ε₀^ε

# F[ε[ε[...ε[ε₀]]]] = ζ₀

# ζ₀ same rules as ε
# F[ε[ε[...ε[ζ₀ + 1]]]] = ζ₁
# F[ζ[ζ[...ζ[ζ₀]]]] = η₀

# Switch to Phi Notation
# φ[α]
# φ₀(x) = ω^x
# φ₁(x) = ε[x]
# φ[2](x) = ζ[x]
# φ[3](x) = η[x]
# ... etc

# Rules -- x = 0
# φ[α](x)[n] = φ^n[α-1](x)[n]
# EXAMPLE: φ₁(0)[2] -> φ₀(φ₀(0))[2] -> φ₀(ω^0)[2] -> φ₀(1)[2] -> ω^1[2] -> ω[2] -> 2[2] -> 4

# Rules -- x > 0
# φ[α](x)[n] = φ^n[α-1](φ[α](x-1) + 1)[n]
# EXAMPLE: φ₁(1)[3] -> φ₀(φ₀(φ₀(φ₁(0)+1)))[3] -> ω^ω^ω^(ε₀+1)

# φ[φ[...φ[φ[0](0)](0)](0)](0) = Γ₀
# Γ[Γ[...Γ[Γ[0](0)](0)](0)](0) = β₀

# Switch to Extended Veblen Notation
# φ(α,x) = φ[α](x)
# φ(1,x) = ε[x]
# φ(2,x) = ζ[x]
# φ(n,α,x)
# φ(1,0,x) = Γ[x]
# φ(1,1,x) = β[x]
# ETC

# Small Veblen Ordinal
# SVO(n)
# SVO(0) = φ(1)
# SVO(1) = φ(1,0)
# SVO(2) = φ(1,0,0)
# SVO(3) = φ(1,0,0,0)
# ETC


# F [Theta · (Ω^ω · ω)] = TREE Sequence
# Xi Function
# Rayo (N) ?

# Learn Bird Notation?

