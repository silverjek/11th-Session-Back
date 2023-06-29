## 1. Django DRF

<br/>

### 댓글 수정과 삭제 기능 구현 과제
views.py의 CommentView 클래스에 get을 추가
CommentDetailView 클래스 생성하여 get, put, delete 정의

Serializer는 이전 방식과 달리 댓글마다 고유의 id가 부여되므로 댓글 디테일 확인하고 수정 및 삭제할 때 게시물의 id 받지 않아도 가능!
-> 그래서 url에서 int:pk 하나만 받아옴

<br/>

