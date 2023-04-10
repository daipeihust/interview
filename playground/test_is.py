a = [1, 2, 3]
b = a
print('a==b:', a==b)
print('a is b:', a is b)

a[2] = 100
print('a:', a)
print('b:', b)

b = [1, 2, 100]
print('a==b:', a==b)
print('a is b:', a is b)
print('a type', type(a))
print('b type', type(b))
