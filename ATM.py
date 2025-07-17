balance = 10000

while True:
    num = input("사용하실 기능의 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료): ")

    if num == '4': # 4번 종료 기능
        break

print(f'서비스를 종료합니다. 현재 잔액은 {balance}')