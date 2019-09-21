import sys
import glob
import os

#glob : 지정된 위치에서 패턴과 일치하는 모든 문장을 찾는다> 폴더를 지정.
#os   : 하나 이상의 경로를 구성하는 요소들을 합친다.
#그래서 두개를 함께 쓴다.

input_path = sys.argv[1]

for input_file in glob.glob(os.path.join(input_path, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))

# $python3 morning3.py /Users/bomilee/Documents/GitHub/python_basic/day_05 
# cmd에서 절대경로 확인 $pwd
