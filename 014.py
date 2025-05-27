# dictionary 字典

user = {
    'key': 'value',
    '鍵':'值',
    'name': 'John',
    'email': 'asdf@gmail.com'
}

# print(user)
# print(user['key'])
# print(user['鍵'])
# print(user['name'])
# print(user['email'])

# print(user.keys())
# print(user.values())
# print(user.items())
#
# for k in user.keys():
#     print(k)
#
# for v in user.values():
#     print(v)
#
# for k,v in user.items():
#     print(f'{k}:{v}')

users = [
    {
        'name': 'John',
        'email': 'asdf@gmail.com',
        'phone': '0987654321'
    },
    {
        'name': 'Mary',
        'email': 'mary@gmail.com',
        'phone': '0912876321',
    },
    {
        'name': 'Ponny',
        'email': 'dksjfksj@gmail.com',
        'phone': '0982321732'
    }
]
# print(users[1]['phone'])
# print(users[-1]['name'])

# for user in users:
#     print(user['name'])
#     print(user['email'])

for user in users:
    for k,v in user.items():
        print(f'{k}:{v}')
    print('--------------------------------------')