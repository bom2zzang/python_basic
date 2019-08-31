'''
pwd = input("비밀번호는 무엇?")
if pwd == '0808':
    print("문이 열리네요....\n ㅎㅎㅎㅎㅎ")
else : #생략가능
    print("x")
'''
'''
x = 10
if x == 10:
    print("x에 있는 숫자")
    #    print(x) 들여쓰기 이렇게 하면 오류남... unexpected indent
    print(x)
'''
'''
x = 10
if x == 10:
    print("x에 있는 숫자")
print(x)    #참 거짓 상관없이 무조건 출력되는 오류
'''
'''
print('숫자입력해')
a = int(input())

if a == 0:
    print("0은 나눗셈에 이용x")
else :
    print('3/',a,'=',3/a)
'''
'''
print("아이 태어난지 몇개월?")
month = int(input())

if month < 1 :
    print("결핵 예방접종 대상")
if month < 2 :
    print("B형간염 예방접종 대상")
if 2 <= month < 6 :
    print("파상풍 예방접종 대상")
if 2 <= month < 15 :
    print("폐렴구균 예방접종 대상")
'''
'''
day = input("요일입력 :")

if day == '월':
    print("mon")
elif day == '화':
    print("tu")
elif day == '수':
    print("w")
elif day == '목':
    print("th")
elif day == '금':
    print("fri")
elif day == '토':
    print("sa")
elif day == '일':
    print("sun")
else :
    print("잘못입력")
'''
'''
import datetime

now = datetime.datetime.now()
#print(now.year,'년')
#print(now.month,'월')
#print(now.day,'일')
#print(now.hour,'시')
#print(now.minute,'분')
#print(now.second,'초')
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
print(now)
'''
'''
import datetime

now = datetime.datetime.now()
if now.hour >= 12:
    hgb = "오후"
else:
    hgb = "오전"

print(hgb)
print("현재 시간은 {} {}시 {}분 {}초".format(hgb, now.hour, now.minute, now.second))

'''
'''
import datetime

now = datetime.datetime.now()
nm = now.month
if 3 <= now.month < 6:
    ss = "봄"
elif 6 <= now.month < 9:
    ss = "여름"
elif 9 <= now.month < 11:
    ss = "가을"
elif 11 <= now.month < 12 or 1 <= now.month < 3  :
    ss = "겨울"
else:
    ss = "???"

print(nm,"월은 ",ss,"입니다.")
'''
'''
#방법1

su = int(input("숫자를 입력해줘요"))

if su/2 == 0:
    print("짝")
else:
    print("홀")
'''
'''

#방법2
su = input("숫자를 입력해줘요")
lc = su[-1]

if lc == 0 or lc == 2 or lc ==4 or lc == 6 or lc == 8:
    print("짝")
else:
    print("홀")
'''
'''
#방법3
su = input("숫자를 입력해줘요")
lc = su[-1]

if lc in '02468':
    print("짝")
else:
    print("홀")
'''
'''
hj = float(input("점수"))

if hj == 4.5:
    pg = "신"
elif 4.2 <= hj < 4.5:
    pg = "교수님의 사랑"
elif 3.5 <= hj < 4.2:
    pg = "현체제의 수호자"
elif 2.8 <= hj < 3.5:
    pg = "일반인"
elif 2.3 <= hj < 2.8:
    pg = "일탈을 꿈꾸는 소시민"
elif 1.75 <= hj < 2.3:
    pg = "오락문화의 선구자"
elif 1.0 <= hj < 1.75:
    pg = "불가촉천민"
elif 0.5 <= hj < 1.0:
    pg = "자벌레"
elif 0 < hj < 0.5:
    pg = "플랑크톤"
else:
    pg = "시대를 앞서가는 혁명의 씨앗"

print(pg)
'''
'''
nm = input("이름\n")
he = int(input("키\n"))
we = int(input("몸무게\n"))

bmi = we/(he/100)**2

if bmi > 30:
    gb ="고도비만"
elif bmi > 25:
    gb ="비만"
elif bmi > 23:
    gb ="과체중" 
elif bmi > 18.5:
    gb ="정상"
else:
    gb ="저체중"

print(nm,'님의 키는' ,he,"cm 이고 몸무게는" ,we,"kg 입니다.\n BMI지수는",bmi,"입니다. \n",gb,"입니다.")
'''
'''
gd = float(input("수능 평균 등급 : "))

if gd > 2:
    print("수능 최저 기준을 만족하지 않았습니다.\n 불합격입니다.")
else:
    print("수능 최저기준을 만족합니다. \n 합격입니다.")
'''
'''
#체력장(모두만족시 합격)
_100m = float(input("100m기록(초)"))
_1000m = float(input("1000m기록(초)"))
up = int(input("윗몸일으키기 기록(회))"))
rile = float(input("좌우 악력기록(kg))")) #right left
arm = int(input("팔굽혀펴기 기록(회))"))

if _100m >= 13.6 and _1000m >= 237 and up >= 51 and rile >= 56 and arm >= 46:
    print("합?")
else:
    print("불합")
'''
'''
#자판기
print("사이다700/콜라800/물1200 \n 돈을 넣어주세요.")
input_money = int(input())
select_drink = int(input("선택 사이다1/콜라2/물3"))

if select_drink == 1:
    drink = "사이다"
    output_money = input_money - 700
elif select_drink == 2:
    drink = "콜라"
    output_money = input_money - 800
elif select_drink == 3:
    drink = "물"
    output_money = input_money - 1200

if output_money < 0:
    print(drink," 뽑을 수 없습니다. \n 잔돈" ,input_money,"원을 반환합니다.")
else:
    print(drink,"나왔다 덜컹 \n 잔돈" ,output_money,"원을 반환합니다.")
'''

#자리수확인
su = int(input("자연수를 입력하세요"))

if su < 10:
    print("1")
elif su < 100:
    print("2")
elif su < 1000:
    print("3")
else:
    print("3이상")

print(len(str(su)))

'''
#5명의심사위원점수> 최대,최소값제거 >나머지값의평균구하기
point1 = float(input("점수1:"))
point2 = float(input("점수2:"))
point3 = float(input("점수3:"))
point4 = float(input("점수4:"))
point5 = float(input("점수5:"))

point = [point1,point2,point3,point4,point5]

point.remove(max(point))
point.remove(min(point))

print("평균: ",sum(point)/3,"점")
'''
'''
num = input("점수입력(스페이스바 이용").split()
runflag = True

if runflag:
    maxi= max(num)
    mini= min(num)
    a,b,c,d,e=[float(x) for x in num]

    avg = (((a+b+c+d+e)-(float(mini)+float(maxi)))/3)
    print(avg)
'''
'''
num = input("4개의 숫자입력:")

if len(num) != 4:
    print("패스워드를 4자리로 입력하세요.")
else:
    num = str(num)
    #numlist = [int(num[0]),int(num[1]),int(num[2]),int(num[3])]
    #print(numlist)

    if num.isnumeric() :
        a = int(num[0])
        b = int(num[1])
        c = int(num[2])
        d = int(num[3])

        if(a == b or a == c or a == d) \
            or (b == c or b == d) or (c == d):
                print("중복된 숫자는 사용할 수 없습니다.")
        
        elif( b == a+1 or c == b+1 or d == c+1) \
            or (b == a-1 or c == b-1 or d == c-1):
                print("연속으로 증가하거나 감소하는 숫자는 사용할 수 없습니다.")
    else:
        print("입력한 값이 숫자가 아닙니다.")
'''
'''
num = input("4개의 숫자로 암호를 입력:")

if num[0] == num[1] :
    print("암호에 중복된 숫자는 사용할 수 없습니다.")
elif num[0] == num[2] :
    print("암호에 중복된 숫자는 사용할 수 없습니다.")
elif num[0] == num[3] :
    print("암호에 중복된 숫자는 사용할 수 없습니다.")
elif num[1] == num[2] :
    print("암호에 중복된 숫자는 사용할 수 없습니다.")
elif num[1] == num[3] :
    print("암호에 중복된 숫자는 사용할 수 없습니다.")
elif num[2] == num[3] :
    print("암호에 중복된 숫자는 사용할 수 없습니다.")
'''
