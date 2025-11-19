10. MCD y MCM
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)
