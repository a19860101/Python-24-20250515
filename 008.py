s = input('請選擇需要轉換的貨幣，美金轉台幣按0，台幣轉美金按1:')
d = input('請輸入金額:')

rate = 30.78

if s == '0':
    result = float(d) * rate
    print(f'美金{d}約等於台幣{result}元')
else:
    # result = float(d) // rate
    result = round(float(d) / rate, 1)
    print(f'台幣{d}約等於美金{result}元')