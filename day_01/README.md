# jupyter notebook
***
* 시작  
terminal >  
$jupyter notebook  *(기본브라우저로 설정해둔 브라우저로 열림)*
오른쪽 위 new>python3 으로 입장.  
소스 디렉토리 확인
    ~~~
    %pwd    
    ~~~

* 연습1 -이동  
    ~~~
    import webbrowser  
    url='www.naver.com'  
    webbrowser.open(url)  
    ~~~
    shift+enter > naver로 이동

    만약 이동하지 않는다면  
    나의 크롬버전과 사이트 크롬버전 체크  
    크롬드라이버에서 맞는 버전 받아서 재시도  
    <https://chromedriver.storage.googleapis.com/index.html?path=76.0.3809.25/>  

* 연습2 -검색
    ~~~
    import webbrowser    

    n_sc_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="  
    sc_word = '야호'

    url = n_sc_url + sc_word  
    webbrowser.open_new(url)  
    ~~~

    ~~~
    import webbrowser
     
    n_sc_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="  
    n_list = ['이천 반도체','이천 쌀','이천 도자기','이천 복숭아']  
    
      for search in n_list :  
          webbrowser.open_new(n_sc_url + search)
    ~~~
    ~~~
    import webbrowser  

    urls = ['www.naver.com','www.daum.net','www.nate.com']  

    for url in urls :  
         webbrowser.open_new(url)
    ~~~

    ~~~
    import webbrowser
    
    urls = ['https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=','https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=','https://search.daum.net/nate?thr=sbma&w=tot&q=']  
    n_list = ['이천 반도체','이천 쌀','이천 도자기','이천 복숭아']  
    
    for url in urls :  
        for search in n_list :  
            webbrowser.open_new(url+search)  
    ~~~

    ~~~
    import webbrowser  
    
    n_sc_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="  
    d_sc_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q="  
    nt_sc_url = "https://search.daum.net/nate?thr=sbma&w=tot&q="  
    g_sc_url = "www.google.com/#q="  
    
    urls = [n_sc_url,d_sc_url,nt_sc_url,g_sc_url]
    n_list = ['이천 반도체','이천 쌀','이천 도자기','이천 복숭아']
    
    i = 0  
    for url in urls :  
        for search in n_list :  
            if n_list[i] == search :  
                webbrowser.open_new(url+search)  
        i = i + 1  
    ~~~

* 조건문.py

***