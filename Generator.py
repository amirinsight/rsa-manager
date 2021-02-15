# Importing smaller parts of the code
import randomZ
import miller
import karatsuba
import euclids

# GCD will be used in calculating e
def gcd(a, b):
    if b == 0:
        if a < 0:
            return -a
        else:
            return a
    else:
        return gcd(b, a % b)

# The main function
def generate():
    # Searching for a prime number (p)
    print("Calculating p...")
    for i in range(34, 7673299):
        temp = randomZ.randomZ(i)
        if miller.prime_check(temp):
            p = temp
            break
        else:
            continue

    # Searching for a second prime number (q)
    print("Calculating q...")
    for i in range(4324, 9876543):
        temp = randomZ.randomZ(i)
        if miller.prime_check(temp):
            q = temp
            break
        else:
            continue

    # Calculating n and phi
    print("Karatsuba is calculating n and phi...")
    n = karatsuba.zarb(p, q)
    phi = karatsuba.zarb(p - 1, q - 1)

    # Choosing e
    # Searching for e starts from half of phi. This way finding e becomes harder for a hacker.
    print("Choosing e and d...")
    def choose_e():
        for i in range(phi // 2, phi - 1):
            if gcd(phi, i) == 1:
                e = i
                return e
            else:
                continue

    # To make calculations faster e is choosen to be 65537
    e = 65537
    if gcd(phi, e) != 1:
        print("Runtime Error.")
        quit()
    #e = choose_e()
    # Finding d using euclids algorithm
    d = euclids.findmi(e, phi)
    P = (e, n)
    S = (d, n)
    print("Public Key: ", P)
    print("Private Key:", S)

    # Writing in file
    with open("Last RSA Keys.txt", 'w') as file:
        file.write("Public Key:")
        file.write(str(P))
        file.write("\n")
        file.write("Private Key:")
        file.write(str(S))
    print("Note: Keys are saved in (Last RSA Keys.txt) for later usage.")