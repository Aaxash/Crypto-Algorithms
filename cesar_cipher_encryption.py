plain = input("Enter Plain Text :")
key = key = int(input("Enter key :"))


def encipher(plain,key):
    cipher = ""
    for i in plain:
        if i.isalpha():
            a = ord(i) + key
            if i.isupper() and a > 90:
                # encoding upper case plain text
                cipher += chr(a - 26)
            elif i.islower() and a > 122:
                # encoding lower case plain text
                cipher += chr(a - 26)
            else:
                cipher += chr(a)
        else:
            # plain text other than a-z,A-Z
            cipher += i

    return cipher


print(encipher(plain,key))
