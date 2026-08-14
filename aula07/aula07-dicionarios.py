eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos',
}
print(eng2sp)
print(eng2sp['one'])

print('one' in eng2sp)

#dicionario como uma colecao de contadores
s = 'ovo'
d = {}
c = 'o'

def contar_let(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(contar_let)

