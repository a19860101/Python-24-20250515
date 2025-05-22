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