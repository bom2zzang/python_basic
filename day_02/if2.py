'''
#주민번호

num = input("주민번호 -빼고 입력")
num = int(num[7:9])

if 0 < num <= 8:
    print("서울")
elif 8 < num <=13:
    print("부산")
elif 13 < num <=16:
    print("인천")
elif 16< num <=26:
    print("경기")
elif 26 < num <=35:
    print("강원")
elif 35 < num <=48:
    print("충청")
elif 48 < num <=67:
    print("전라")
elif 67 < num <=92:
    print("경상")
elif 92 < num <=95:
    print("제주")
else:
    print("잘못입력하셨")
'''
'''
#pass키워드
number = input("정수입력: ")
number = int(number)
print(number)
print(type(number))

if number > 0:
    pass
else:
    pass
'''
