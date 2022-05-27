c = '1010100100101010101111001000110101110101001001100111010'
p = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
c_count = int(len(c) / 5)

for i in range(c_count):
    p.append(c[(i * 5):i * 5 + 5])

print(p)

for j in p:
    p[p.index(j)] = alphabet[int(j, 2) - 1]

print(''.join([str(elem) for elem in p]))
