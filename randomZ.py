# Imports. System time is used to generate seeds
from datetime import datetime


# Base of lcg algorithm to generate random numbers
def lcg(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        return seed


# Using system time as a seed. I made it into a function so that it's value can change over time.
def seedmaker():
    now = datetime.now()
    alan = now.strftime("%H%M%S")
    return int(alan)


def randomZ(i=0):
    # MMIX: A trio of mod, a and c that is used in lcg.
    mod = 18446744073709551616
    a = 6364136223846793005
    c = 1442695040888963407
    myrand = ''

    # Putting blocks of random numbers together to make it bigger.
    # 160 character length is chosen so that: p * q > 309
    # I added len(myrand) to seed since seed doesnt change
    # Also added i so when randomZ is used in loops we can have different numbers
    while len(myrand) < 160:
        lc = lcg(mod, a, c, seedmaker() + len(myrand) + i)
        myrand = myrand + str(lc)

    # To return odd numbers only:
    myrand = int(myrand)
    if myrand % 2 == 0:
        return myrand - 1
    else:
        return myrand

# To use randomZ: import randomZ, var = randomZ.randomZ(some optional number to add more randomness)
# Note that randomZ.randomZ() returns an odd number
