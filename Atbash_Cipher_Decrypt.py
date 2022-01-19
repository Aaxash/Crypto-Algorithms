word = input("Enter the cipher text: ")


def atbash_Decrypt():
    c = ''
    for i in word:
        if i.isalpha():
            a = ord(i) - 25
            if i.isupper() and a < 65:
                c += chr(65 + (65 - a))
            elif i.lower() and a < 97:
                c += chr(97 + (97 - a))
            else:
                c += chr(a)
        else:
            c += i
    return c


print(atbash_Decrypt())
