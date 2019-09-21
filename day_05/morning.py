#셔뱅 > 유닉스.리눅스 
#! usr/bin/env python3

import sys
#sys모듈을 사용하면 리스트형식의 argv변수를 사용할 수 있다.
#이 변수는 명령 줄 인수들로 구성된 리스트를 파이썬 스크립트로 가져온다.
#다른 리스트와 마찬가지로 argv는 인덱스를 갖는다.

print("Putput : music1.txt")
print()

#스크립트 파일 실행시 이름을 지정할 수 있다. input()함수와 동일..
#sys.argv[0] sys.argv[1] sys.argv[2]
#sys.argv[0]은 스크립트 파일명을 의미하기 때문에 스크립트 파일 내에서 사용 금지.
input_file = sys.argv[1]
filereader = open(input_file, 'r')  #읽기전용, open을 했으면 close를 해줘야함 ! 
# r:읽기전용 / w:쓰기전용 / a:추가모드(기존파일보호 , 마지막줄에 추가)

for row in filereader:
    print(row.strip())
filereader.close()

# $python3 morning.py music1.txt

