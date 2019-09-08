'''
#쥐 총 몇마리
#쌀 100통 > 1통에 1kg =  1000g
#암수 한쌍
#쥐 한마리 하루 20g
#10일마다 쥐 2배 증가
#며칠만에 쌀 0, 그 때 쥐의 수

rice = 100000
mouse = 2
day = 0

while rice > 0:
    day += 1
    rice = rice - (mouse * 20)

    #10일체크
    if (day % 10) == 0:
        mouse *= 2
print("{}일 경과 {}마리 쥐".format(day,mouse))
'''
