coffee = 10
money = 300
print("현재 제공 가능한 커피는 %d 잔입니다." % coffee)
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 커피 판매를 중지합니다.")
        break