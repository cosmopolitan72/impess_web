# 소개: flask 기반으로 만든 간단한 로그인 페이지입니다.

## 폴더 구조 
myproject/
├── app.py
├── models.py
├── forms.py
├── templates/
│ ├── hello.html
│ ├── register.html
│ └── register_success.html
├── db.sqlite
└── README.md

## 주요 기능
- 사용자 회원가입 (비밀번호 해시 처리 / SHA-256)
- 로그인/로그아웃 (세션 기반)
- SQLite 데이터베이스 사용

## 패키지 설치

1. 가상환경 설정
(1) python -m venv venv
(2) venv\Scripts\activate

2. pip install flask, pip install flask-wtf, pip install flask-sqlalchemy, pip install werkzeug

3. app.py에서 디버그 -> http://127.0.0.1:5000 접속 

### 전체 흐름 

*** 회원이 없는 경우 ***
회원가입 -> GET/register -> register.html -> Post/register(사용자의 정보 전송) -> 비밀번호 해시처리 + DB저장 -> register_success.html

*** 로그인 상태에서 ***
GET /logout -> session.pop -> redirect(로그인 화면으로)

 
####
html 파일은 모두 templates 폴더 안에 들어가 있어야 합니다~!

sqlite3 db.sqlite (db.sqlite 생성 안될 경우 터미널에 입력) 
