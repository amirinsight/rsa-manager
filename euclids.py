def extengcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extengcd(b % a, a)
        z = x - (b // a) * y
        return (g, z, y)

def findmi(a, m):
    g, x, y = extengcd(a, m)
    return x % m

# To use findmi(mod inverse): import euclids, var = euclids.findme(x, y)
