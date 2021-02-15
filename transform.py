#Same as ascii.py but unused.

def ttn(text):
    bytes = text.encode('utf-8')
    ints = int.from_bytes(bytes, 'little')
    return ints


def ntt(number):
    bytes = number.to_bytes((number.bit_length() + 7) // 8, 'little')
    text = bytes.decode('utf-8')
    return text


# To use transform: import transform, use transform.ttn("text here") to turn text into number
# and transform.ntt(number here) to turn number into text
