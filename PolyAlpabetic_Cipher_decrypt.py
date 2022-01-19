text = input("Enter Cipher Text :")
k = input("Key :")


def poly_alpha_decrypt(cipher, key):
    p = ""
    x, j = 0, 0
    for i in cipher:
        if i.isalpha() and i.upper():
            x = ord(i) - (ord(key[j].upper()) - 65)
        elif i.isalpha() and i.lower():
            x = ord(i) - (ord(key[j].lower()) - 97)
        else:
            p += i
            continue
        if i.isupper() and x < 65:
            x += 26
        elif i.islower() and x < 97:
            x += 26
        p += chr(x)
        j += 1
        if j > len(key) - 1:
            j = 0
    return p


print("Plain text : " + poly_alpha_decrypt(text, k))
