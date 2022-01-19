word = input("Enter the plain text: ")


def atbash_encrypt():
    c = ''
    for i in word:
        if i.isalpha():
                a = ord(i) + 25
                if i.isupper() and a>90:
                    c += chr(90 -(a - 90))
                elif i.lower() and a>122:
                    c += chr(122 -(a - 122))
                else:
                    c += chr(a)
        else:
            c += i
    return c


print(atbash_encrypt())