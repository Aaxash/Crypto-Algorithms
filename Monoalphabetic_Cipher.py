word = input("Enter the plain text: ")
letters = {
    'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c', 'f': 'x', 'g': 'z', 'h': 'a',
    'i': 's', 'j': 'd', 'k': 'f', 'l': 'g', 'm': 'h', 'n': 'j', 'o': 'k', 'p': 'l',
    'q': 'p', 'r': 'o', 's': 'i', 't': 'u', 'u': 'y', 'v': 't', 'w': 'r', 'x': 'e',
    'y': 'w', 'z': 'q'
}


def get_key(value):
    for key, val in letters.items():
        if val == value:
            return key


def monoalphabetic_encrypt():
    c = ''
    for i in word.lower():
        if i.isalpha():
            c += letters.get(i)
        else:
            c += i
    return c


print("Cipher Text :" + monoalphabetic_encrypt() + "\n")
