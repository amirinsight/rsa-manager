# See transform.py for more info
import transform
import ascii

# M(message in numbers) ** e(key[0]) mod n(key[1]) = C(output)
def encrypt():
    message = input("What is your secret message?")
    key = [0, 0]
    key[0] = int(input("Now please type/paste e(public key) here:"))
    key[1] = int(input("Now please type/paste n here:"))

    block_size = 20
    if len(message) % block_size == 0:
        block_count = len(message) // block_size
    else:
        block_count = (len(message) // block_size) + 1
    blocks = [0] * block_count
    coded = [0] * block_count
    for i in range(0, block_count):
        blocks[i] = message[i * block_size:(i + 1) * block_size]


    print("Encoding. Please wait...")
    for i in range(block_count):
        #numeric = transform.ttn(blocks[i])
        numeric = ascii.TextToNum(blocks[i])
        coded[i] = pow(numeric, key[0], key[1])


    print("Coded Message:")
    for i in range(0, block_count):
        print('Part',i+1,': ', end='')
        print(coded[i])
