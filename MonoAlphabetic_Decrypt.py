word = input("Enter the cipher text: ")
letters = {
    'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c', 'f': 'x', 'g': 'z', 'h': 'a',
    'i': 's', 'j': 'd', 'k': 'f', 'l': 'g', 'm': 'h', 'n': 'j', 'o': 'k', 'p': 'l',
    'q': 'p', 'r': 'o', 's': 'i', 't': 'u', 'u': 'y', 'v': 't', 'w': 'r', 'x': 'e',
    'y': 'w', 'z': 'q'
}


def key():
    k = ""
    v = ""
    for i in letters.keys():
        k += i
    for j in letters.values():
        v += j
    return v


def get_key(value):
    for key, val in letters.items():
        if val == value:
            return key


def monoalphabetic_decrypt():
    c = ''
    for i in word:
        if i.isalpha():
            c += get_key(i)
        else:
            c += i
    return c


print("Plain Text:" + monoalphabetic_decrypt())
