# coffee.py

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요(원): "))
    if money == 300:
        print("커피를 제공합니다.")
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d원를 주고 커피를 제공합니다." % (money-300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 제공하지 않겠습니다.")

    print("현재 제공 가능한 커피의 양은 %d잔 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
