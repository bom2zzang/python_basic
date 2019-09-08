***
## DOCKER
* <https://github.com/docker/toolbox/releases>

## SQL
* 사용자 정보 확인
~~~
    $ SELECT HOST,USER,PASSWORD FROM MYSQL.USER;
~~~
* 원격접속
    + *USER1이 localhost로 설정되어있으면 접속에러 발생*  
    
~~~
    $ MYSQL -U USER1 -P --PORT 3309 --HOST 192.168.0.253
~~~
* 클라이언트 프로그램으로 DB서버 제어하기
~~~
    > MYSQLADMIN.EXE -u root -p CREATE WHITE; (win)
    > MYSQLADMIN -u root -p create white; (mac)
~~~
* 실습1
~~~
#!/usr/bin/env python3 
#셔뱅(주석문이아님): python3을 치지 않아도 python3로 실행(리눅스,유닉스)
~~~

* 실습2
~~~
CMD > pip install mysqlclient 

    $ CREATE DATABASE my_suppliers;
    $ SHOW DATABASES;
    $ USE my_suppliers;
    $ CREATE TABLE 
    (Supplier_Name VARCHAR(20),
    Invoice_Number VARCHAR(20),
    Part_Number VARCHAR(20),
    Cost FLOAT,
    Purchase_Date DATE);
    $ DESC Suppliers;
    $ CREATE USER ‘사용자명’@’localhost’ IDENTIFIED BY ‘암호’; 
    $ GRANT ALL PRIVILEGES ON my_suppliers.* TO ‘사용자명’@’localhost’; 
    $ FLUSH PRIVILEGES; 
~~~

* jupyter notebook
~~~
    !pip install pandas     #데이터분석
    !pip install xlrd       #
    !pip install xlsxwriter #
    !pip install matplotlib # 
~~~
* 설치 후 
~~~
import pandas as pd
df = pd.read_excel("학생시험성적.xlsx")
df
~~~

***