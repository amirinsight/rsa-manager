# See transform.py for more info
import transform
import ascii

# C(secret in numbers) ** d(key[0]) mod n(key[1]) = M(output)
def decrypt():
    key = [0, 0]
    key[0] = int(input("Now please type/paste d(private key) here:"))
    key[1] = int(input("Now please type/paste n here:"))
    print("Now please type/paste the coded message BLOCK by BlOCK.")
    coded = []
    while True:
        try:
            putin = input("Type/Paste a block. Type in 'stop' when you are done:")
            if putin == "stop":
                break
            else:
                coded.append(int(putin))
        except TypeError:
            print("Invalid Input. Try again.")

    print("Decoding. Please wait...")
    message = [0] * len(coded)
    for i in range(0, len(coded)):
        numeric = pow(coded[i], key[0], key[1])
        #message[i] = transform.ntt(numeric)
        message[i] = ascii.NumToText(numeric)

    print("Decoded message:")
    for i in message:
        print(i, end="")
