## 1. Django 기초 README

<br/>

# 1. 코드 Summary
먼저, 참고한 자료의 코드를 먼저 VS Code에 붙여넣고 오류가 생기는 부분들을 하나씩 고쳐보았습니다. 특히 변수 명이 다른 부분들이 있어서 어디를 고쳐서 원래 작성했던 코드와 맞춰야하는지 고민했습니다. 자세히는, 참조 한 코드에 검색 필터를 이전에 models.py에 작성했던 title, upload_time, content로 바꿔주었습니다. 또한 content_list와 board 라는 필드에 쓰인 코드도 스터디 때 작성한 Posting을 기준으로 바꿔주었습니다. 그리고 검색창 html은 참조 문서의 코드를 복사해 사용했습니다. 더 나아가 list.html에 코드를 추가해 웹페이지에 들어가면 바로 뜨는 창에 검색창을 만들고싶어 또 다른 자료를 참고해 한 list.html에 새로 만든 검색창 search.htlm을 include 하였습니다.

<br/>

## 2. Key Changes

<br/>

## 3. Reference
https://ghqls0210.tistory.com/53
-> 검색 기능을 구현할 때에 urls.py와 view.py에 어떤  코드가 들어가는지 참고했습니다. 검색 기능과 pagination 기능을 참조했고, 검색창 html을 참조했습니다.
https://mrlee-sub.tistory.com/267
-> 참조한 코드를 이전 스터디에서 작성한 코드에 합치려고 수정하다보니 UnboundLocalError가 자주 발생하여 이를 해결하기 위해 참조했습니다.
https://velog.io/@jewon119/Django-기초-Search-Bar-기능-구현
-> 메인으로 뜨는 페이지에 검색 바를 넣고싶어 html을 참조하였고, 검색 바에 'Search by title'이라는 글씨를 넣는 방법을 참조했습니다.

<br/>

## 4. Report
https://www.notion.so/likelion-ewha-11/c1db44b457bf44f98d9a536300e37d69?pvs=4

<br/>
