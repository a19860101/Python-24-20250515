# 大樂透電腦選號
# 1-49, 6+1

import random

result = []

while len(result) < 7:
    n = random.randint(1,49)
    if n not in result:
        result.append(n)

# result.sort()
print(result)

spe = result[-1]
com = result[:-1]
print('大樂透第xx期')
print(f'電腦選號號碼為:{com}，特別號為{spe}')