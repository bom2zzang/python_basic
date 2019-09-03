'''
#무한루프
while True:
    print("$", end='')
'''

'''
#1에서 30까지의 숫자 출력
l = list(range(1,31))
print(l)

#1에서 100까지 홀수만
h = list(range(1,101,2))
print(h)
'''
'''
#in 연산자
array = [273,32,103,57,52]

print("array:", array)  #list에 값이 있는지 True False로 출력됨
print("273 in array", 273 in array)
print("99 in array", 99 in array)
print("100 in array", 100 in array)
print("52 in array", 52 in array)

#not in > in연산자와 반대
'''
'''
#리스트에 반복문 적용
array = [273,32,103,57,52]

for el in array:
    if el >100:
        print(el)
'''
'''
for ch in "안녕하세요":
    print("-",ch)
'''
'''
dic={}
dic['파이썬']='www.python.org'
dic['마쏘']='www.microsoft.com'
dic['애플']='www.me.com'

print(dic['파이썬'])    #www.python.org
print(dic.keys())
print(dic.values())
print(dic.items())

dic.pop('애플') # == del dic['애플']
print(dic.items())
'''
'''
#update() 함수로 딕셔너리 키와 값을 결합
#copy() 함수로 딕셔너리 복사.
'''
'''
#터틀로 6개의 원 그리기
import turtle
t= turtle.Turtle()

for count in range(6):
    t.circle(100)   #100크기의 원을 그린다
    t.left(360/6)   #360도를 6등분 
'''
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","몇각?:")
n = int(s)

for x in range(n):
    t.forward(80)
    t.left(360/n)
'''
'''
#매개변수에 넣는 숫자
#방법1 : 범위선언 range(<숫자>)
print(range(5), list(range(5)))
print(range(10), list(range(10)))
print()
#방법2 : range(<숫자>,<숫자>)
print(range(0,5),list(range(0,5)))
print(range(5,10),list(range(5,10)))
print()
#방법3 : range(<숫자>,<숫자>,<숫자>)
print(range(0,10,2),list(range(0,10,2)))
print(range(0,10,3),list(range(0,10,3)))
print()
'''
'''
#2부터 100까지의 짝수출력
for pr in range(2,101,2):
    print(pr)
'''
'''
#사용자가 1입력 홀수, 2입력 짝수를 100까지 출력

inx = int(input("1 또는 2를 입력하세요."))
for pr in range(inx, 101,2):
    print(pr, end=' ')
'''
'''
#피보나치수열
#1항:0/2항:1/3항:1항+2항
a = 0
b = 1
x = 0
for pr in range(100):
  print(pr, end = ' ')
  print(x)
  x = a + b
  a = b
  b = x
  #0부터 나오게 수정..
'''
'''
bob = ['아침','점심','저녁','야식']

inday = int(input("며칠이 지났?질문이 뭐야?"))
#방법1
#for bobs in bob*inday:
#    print(bobs)

#방법2 - 따라친건데 
i = 1
j = 0
while i > 0:
    i = int(input("종료('0') 몇일이 지났습니까: "))
    j = i

    while j > 0:
        for k in bob :
            print(k)
        j = j-1
'''
'''
#아래의 결과가 출력되도록 for문
#0 0 0 0 0
#0 1 2 3 4
#0 2 4 6 8
#0 3 6 9 12
#0 4 8 12 16

for i in range(5):
    print()
    for j in range(5):
        print(i*j, end=' ')
'''
'''
#구구단계산
inx = input("구구단 몇단?")
print("구구단",inx,"단")
for i in range(1,10):
    print(i)
    for j in inx:
        print(inx,"x",i,"=",int(inx)*int(i))
'''
'''
#list에 점수 5개 저장
#70이상1급/60이상2급/이하불합
sc = [78,100,50,40,88]
num = 0
for gd in sc:
    if gd >= 70:
        num += 1
        print(num,"번 학생은 1급 입니다.")
    elif gd >= 60:
        num += 1
        print(num,"번 학생은 2급 입니다.")
    else:
        num += 1
        print(num,"번 학생은 불합격 입니다.")
'''
'''
#while
while True:
    print("반복을 계속?(예/아니오)")
    answer = input()

    if answer == '예':
        print("반복")
    elif answer == '아니오':
        break
    else:
        print('제대로다시입력')
'''
'''
list_test = [1,2,1,2]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)        #[1, 1]
'''
'''
#1~30까지 중에서 3의 배수에 해당하는 값은 지운다
#내가 한것 
list_test = list(range(1,31))
xs = 1
xx = 3  #3의배수
while True:
    #print(3*xs)
    list_test.remove(xx*xs)
    xs += 1
    if xx*xs > 30:
        break

print(list_test)
'''
'''
#선생님
a = list(range(1,31))
i=0
while i < len a:
    if a[i] % 3 == 0:
        a.remove(a[i])
    i += 1
print(a)
'''
'''
#1~30 짝수만 출력
su = list(range(1,31))

i=0
while i < len(su):
    if su[i] % 2 != 0:
        su.remove(su[i])
    i += 1
print(su)
'''
'''
#시간
import time

output = 0
target_tick = time.time() + 5
while time.time() < target_tick:
    output += 1
print("5초 동안 반복한 횟수:", output)
'''
'''
import time
#유닉스 타임을 구합니다. 
print(time.time())      #1567316356.2648814
                        # 1분   = 60초
                        # 1시간 = 3600초
                        # 1일   = 3600초
                        # 1달   = 
                        # 1년   = 뭐야 패스
'''
'''
pw = 'pythonisgood'

while True:
    inpw = input("암호를 입력하세요")
    if pw == inpw:
        print('성공')
        break
    elif inpw == 'gu':
        print('포기')
        break
'''
'''
#가우스 계산기 잘못이해하고 만든거..ㅋ
su = 0
while True:
    plus = int(input("종료-1/숫자입력: "))
    if plus == 1:
        break
    else:
        su= su+plus
        print(su)
'''
'''
#가우스 계산기
num =""
while num != 1:
    num = int(input("종료-1/숫자입력:"))
    i = 1
    sum = 0

    while i < num + 1:
        sum += i
        i += 1
    print(sum)
'''
'''
# 1~100홀수만 while로,.,, 구만,,,구만회...
i = 1
while i  < 101:
    print(i)
    i +=2
'''
'''
i = 1
while i < 31:
    print(i%4, end=' ') 
    i += 1    
'''
'''
#구구단 업그레이드
num = ""

while True:
    num = int(input("몇단을계산할까요1-9 :"))
    x = 1
    if 1 <= num < 10:
        while x < 10:
            print(num,"x",x,"=",num*x)
            x += 1
    else:
        break
'''
'''
#구구단선생님
x = ""

while (x is not 0):
    x = int(input("1-9사이 입력"))

    if x == 0:
        break
    if not (1 <= x <= 9):
        print("잘못 다시")
        print()
        continue
    else:
        print()
        print("구구단" + str(x) +"단을 출력합니다.")

        for i in range(1,10):
            print(str(x)+"x"+str(i)+"="+str(x*i))
        print("몇단을 계산할까요")
        print()

print("구구단 종료")
'''
'''
#최대공약수
# 21 : 1, 3, 7, 21
# 9  : 1, 3, 9
# 두 수의 최대공약수는 3
# 유클리호제법 : a와 b의 최대공약수는 a/b 나눈 나머지와 b의 최대공약수,
# 단 A>B
# 아 나 이해못했어...
# 수학공식이 따로 있다고 한다.

a = int(input("1번수:"))
b = int(input("2번수:"))

if b > a:
    a,b = b,a

while b != 0:
    a = a % b
    a,b = b,a
    
print("최대공약수",a)
'''
'''
#주사위 프로그램
#quit : 종료
#Enter : 주사위 던지기

from random import *

number = 0
print("주사위 시작")

while number != 'quit':
    print(randint(1,6))
    number = input("계속?Enter\n 종료?quit")
'''
'''
#up & down
#컴퓨터가 선택한 랜덤의숫자
#사용자입력
#컴퓨터 updown 출력 (횟수저장)
#맞추면 횟수 출력

from random import *

comselect = randint(1,100)
count = 0

while True:
    userselect = int(input("1~100사이 숫자 입력:"))
    count += 1
    if userselect == comselect:
        print("정답")
        print(str(count)+"회 시도")
        break
    elif userselect < comselect:
        print("up")
    elif userselect > comselect:
        print("down")
'''        



