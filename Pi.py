Lsquare = 0.5 * (2) ** 0.5
r = 0.5


def Leg_calc(n):
    if (n == 2):
        return Lsquare
    else:
        return (((Leg_calc(n - 1) / 2) ** 2) + (r - (r ** 2 - (Leg_calc(n - 1) / 2) ** 2)**0.5) ** 2) ** 0.5


def pi_calc(n):
    print((2 ** n) * Leg_calc(n))


pi_calc(20)