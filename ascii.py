# Used in Encryption and Decryption codes. This module can transform text to a number and number to text

def TextToNum(text):
    num = 0
    for i in range(0, len(text)):
        num += 256 ** (len(text)-1-i) * ord(text[i])
    return num


def NumToText(num):
    text = ''
    while num > 0:
        text += str(chr(num % 256))
        num = num // 256
    # Text ma bar aks mishe bara hamin baraksesh mikonim
    return text[::-1]
