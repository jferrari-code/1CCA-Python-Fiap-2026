t = ('a' , 'b' , 'c' , 'd')
print(t[1:3])

t1 = 'A',
print(t1)

t2 = t1 + t[1:]
print(t2)


# ATRIBUICAO DE TUPLAS
a = 5
b = 10

a, b = b, a
print(a, b)


email = 'fulano@gmail.com'
username, domain = email.split('@')
print(username)
print(domain)