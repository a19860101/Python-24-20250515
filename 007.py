# s = input('請輸入文字:')
#
# print(s)

# 台幣轉美金

s = input('請輸入台幣金額:')
result = float(s) / 30.78
result = round(result, 1)
print(f'台幣{s}約等於美金{result}元')