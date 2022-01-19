text = input("Enter Plain Text :")
k = input("Key :")


def poly_alpha_encrypt(plain, key):
    cipher = ""
    x, j = 0, 0
    for i in plain:
        if i.isalpha():
            if i.upper():
                # encoding upper case plain text
                 x = ord(i) + (ord(key[j].upper()) - 65)
                 if x > 90:
                     x -= 26
            if i.lower():
                # encoding lower case plain text
                x = ord(i) + (ord(key[j].lower()) - 97)
                if x > 122:
                    x -= 26
        else:
            # plain text other than a-z,A-Z
            cipher += i
            continue
        
        cipher += chr(x)
        
        j += 1
        if j > len(key) - 1:
            j = 0

    return cipher


print("Cipher Text : "+poly_alpha_encrypt(text, k))
