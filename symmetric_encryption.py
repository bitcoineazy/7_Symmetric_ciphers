print("Шифр Цезаря")
s = "Hello world!"


def caesar_encode(mes, z):
    return [chr((ord(i) + z) % 65536) for i in mes]


def caesar_decode(mes, z):
    return [chr((65536 + (ord(i) - z) % 65536) % 65536) for i in mes]


a = caesar_encode(s, 10)
b = caesar_decode(a, 10)
print(s, a, "".join(b))

print("Взлом шифра цезаря")


def caesar_hack(mes):
    numdict = {}
    for i in set(mes):
        numdict[i] = mes.count(i)
    chmax = max(numdict.values())
    plist = []
    for k, v in numdict.items():
        if v == chmax:
            plist.append(k)
    for ch in plist:
        yield [chr((65536 + (ord(i) - (ord(ch) - ord(" ")) % 65536)) % 65536)
               for i in mes]


print(*[''.join(i) for i in list(caesar_hack(a))], sep="\n")


def vizhiner_encode(z, m):
    k = z * (len(m) // len(z)) + z[:len(m) % len(z)]
    return list(map(lambda x: x[0] ^ x[1],
                    zip([ord(i) for i in m], [ord(i) for i in k])))


def vizhiner_decode(k, c):
    k = k * (len(m) // len(k)) + k[:len(m) % len(k)]
    return ''.join([chr(i) for i in
                    map(lambda x: x[0] ^ x[1], zip(c, [ord(i) for i in k]))])


print('Шифр Вижинера')
m = "1234567890"
k = "abc"
c = vizhiner_encode(k, m)
print(vizhiner_decode(k, c))
