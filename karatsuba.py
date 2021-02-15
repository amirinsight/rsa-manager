def zarb(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        maxim = max(len(str(x)), len(str(y)))
        m = maxim // 2

        # Do ta addad asli ro mishekanim be 4 ta addad
        a = x // 10 ** (m)
        b = x % 10 ** (m)
        c = y // 10 ** (m)
        d = y % 10 ** (m)

        # Mohasebe bazgashti
        bd = zarb(b, d)
        rest = zarb((a + b), (c + d))
        ac = zarb(a, c)

        result = (ac * 10 ** (2 * m)) + ((rest - ac - bd) * 10 ** (m)) + (bd)
        return result

# To use Karatsuba: import karatsuba, karatsuba.zarb(x,y)
