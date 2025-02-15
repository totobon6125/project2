### 조원 명단

- 프로젝트 참여 명단

|이름|역할|업무|블로그|깃허브|
|------|---|---|---|---|
|김대욱|팀장|회원가입 및 로그인|[블로그](https://blog.naver.com/ackrima)|[깃허브](https://github.com/totobon6125)|
|노지현|팀원|좋아요 기능 구현 및 메인 페이지|[블로그](https://imcodiiing.tistory.com)|[깃허브](https://github.com/jihyeon4956)|
|강권영|팀원|전체적인 CSS|[블로그](https://blog.naver.com/breaker-512)|[깃허브](https://github.com/passbreaker1)|
|김석현|팀원|방명록 CRUD|[블로그](https://disosa.tistory.com/)|[깃허브](https://github.com/disosa)|
    


### 그라운드 룰

- 시간표
    - 의무접속 09:00 ~ 21:00
    - 아침회의 09:00 ~ 09:10 (각자 진행척도 확인 및 회의)
    - 오전학습 09:10 ~ 12:00 (각자 기능구현)
    - 점심시간 12:00 ~ 13:00
    - 오후회의 13:00 ~ 13:10 - 분담 업무에 대한 진척도 확인(완성/시간더필요 등)
    - 오후학습 13:00 ~ 17:30 (각자 기능구현)
    - 저녁미팅 17:30 ~ 18:00 (진척도 조사 및 기술매니저님한테 질문할 것들 정리)
    - 저녁식사 18:00 ~ 19:00
    - 기술미팅 19:00 ~ 20:00
    - 정리시간 20:00 ~ 21:00 (자유로운 회의 및 의견공유)
    - 이후시간 21:00 ~           (자유시간 - 퇴근 / 자습 / 대화 등 자유롭게)
    

### 프로젝트 설명

- 프로젝트 설명
    1. 프로젝트 이름
    :  제주 바당
    
    2. 프로젝트 설명
    :  제주도 해변에 대한 회원들의 코멘트.
    
    3. YouTube 시연 영상
    :  [시연영상](https://www.youtube.com/watch?v=WagydXAS7aA)
    
    

### 와이어 프레임

- 와이어 프레임
    
    [와이어 프레임](https://app.eraser.io/workspace/xW4rMd4Yv5mBr9rds5nj?origin=share)
    

### API 명세서

- API 명세서
    
    [2조 버킷 리스트](https://www.notion.so/89efbf5310e74ecaa2a1ff4247053d3c?pvs=21)
    

### 트러블 슈팅

- 강권영님

|트러블|상황|노력|해결|
|------|---|---|---|
|app.py데이터 받을 때|app.py 맨 아래 줄app.run() 안에 내용이 비어있어서 안되었다.|app.py 맨 아래 줄app.run() 안에 내용이 비어있어서 아되었다.|app.run('0.0.0.0', port=5000, debug=True)넣고 http://localhost:5000 돌리니 된다|
|제주 날씨 api| url의 icon 내용은 이미지 주소였다 data[’icon’]을 변수에 넣고 ${icon} 하면 주소가 나온다 문제는 이미지로 받고 싶은것|기술 매니저님에게 상황 설명 및 조언구함|`안에img태그를 사용해서` 변수에 할당하고 append해줬다|
|조원소개 페이지 만들기|templeats에 적당한 html에 틀만 복사해서 조원 소개html로 꾸며 보기|웹종합에서 배운 리스트와 객체 합친것을 사용해서 forEach로 append하는 것을 해보니 console.log에는 잘 나왔지만 html로 합쳐지지 않았다. 그래서 팀원에게 물어보고 매니저님에게 물어봐서 해결했고 데이터는 잘 나타나지만 꾸미는 것은 생각이 잘 나지 않았다.|내용은 잘 나왔지만 꾸밀 수 있는 테이블의 형태나 배경등이 아쉬웠다. 페이지 형식에 맞는 배경이나 꾸밀 수 있는 부분이 미흡해서 html,css,javascript등 이미 완성된 코드를 보는 것이 익숙했고 맨 화면에 내가 직접 채워 넣으려 할 때는 아무 생각이 안 났다. 좀 더 여러 프로젝트에 참여해 보고 코드를 적용 할 수 있을 정도로 많이 반복해서 공부해야겠다.|

    
- 김대욱님

|트러블|상황|노력|해결|
|------|---|---|---|
|코드 컨벤션|안 정해서 서로 변수명이 다른데 어디가 다른지 찾는게 어려웠습니다.|팀원들과 같이 코드를 뜯었습니다.|코드 컨벤션을 정해서 다시 풀을 받아 코드를 만들었습니다.|
|코드에서 웹 이동 하는 방식의 차이|render_template은 페이지 내용을 생성하여 보여주는 것이고, redirect는 사용자를 다른 페이지로 이동시키는 것인데 이 차이를 명확하게 몰라 사용해서 페이지가 무한 로딩에 걸렸습니다.|redirect 를 사용할 경우 무한 반복이 되거나 이동이 안되는 경우가 있었습니다.|render_template 으로 대체하여 무한 로딩을 풀고 원하는 방향으로 코딩을 했습니다.|
    
- 김석현님
    
    
- 노지현님

|트러블|상황|노력|해결|
|------|---|---|---|
|클라이언트에서 전달받은 좋아요, 싫어요 선택횟수를 MongoDB에 누적적용하기|index.html에서 click 이벤트로 좋아요와 싫어요를 선택할때마다 +1이 되도록 설정했느나 DB반영이 안되어 새로고침시 초기값인 0으로 나옴|화면에 출력되는 value값(let likeCount = parseInt( $(this).nextAll('.like-count').text());)으로 받아옴. -> DB에 반영은 되나 값이 이상하게 변경됨 초기값 0, 선택1 => 1로 변경 DB값 1, 선택2 => 1+2인 3으로 변경되는 문제가 또 발생함|화면에서 좋아요, 싫어요를 클릭했을때 +1을 담아주는 변수를 선언하고 해당 변수의 값을 전달하여 해결함|

    

### 개선할 점

# 😙 **“시간이 있다면” 이런걸 해보고 싶어요!**

- 강권영님
    - 부트스트랩을 자유롭게 사용할 수 있도록 하고 싶습니다.
- 김대욱님
    - 데이터 베이스에 저장되는 user password 에도 암호화 처리되어 데이터 베이스 관리자도 암호를 확인할 수 없게 하고 싶습니다.
- 김석현님
- 노지현님    
    - 지금은 누구나 좋아요, 싫어요를 무한대로 누를 수 있는데 추후에는 사용자의 id값을 식별하여 좋아요 or 싫어요 버튼을 한번만 누를 수 있고 또 내가 누른 버튼을 진하게 변경하여 새로고침을 하더라도 그 상태를 유지하는 기능을 만들고 싶습니다.
