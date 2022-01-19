cipher = input("Enter cipher Text :")
key = int(input("Enter key :"))

def decipher(cipher,key):
    plain = ""
    for i in cipher:
        if i.isalpha():
            a = ord(i) - key
            if i.isupper() and a < 65:
                plain += chr(a + 26)
            elif i.islower() and a < 97:
                plain += chr(a + 26)
            else:
                plain += chr(a)
        else:
            plain += i

    return plain


print("Plain Text:"+decipher(cipher,key))
