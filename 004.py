# 判斷式 條件式

x = 0
# if
if x > 0:
    print('正')

if x > 0:
    print('正')
else:
    print('負')

if x > 0:
    print('正')
elif x < 0:
    print('負')
else:
    print('0')

# 3.10後

s = 123

match s:
    case 0:
        print('星期日')
    case 1:
        print('星期一')
    case 2:
        print('星期二')
    case 3:
        print('星期三')
    case _:
        print('ERROR')