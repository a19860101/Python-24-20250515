# list 串列

a = ['apple', 'banana', 'cat', 'dog', 'elephant']
b = list(['asdf', 'poiu'])
print(type(a), type(b))

# print(a)
# print(a[0])
# print(a[1])
# print(a[2])

print(a[0:2])
print(a[1:4])
print(a[1:])
print(a[:3])
print(a[2:-1])
print(a[-4:-1])


for data in a:
    print(data)

for data in enumerate(a):
    print(data)
#
# for idx, data in enumerate(a):
#     print(idx)