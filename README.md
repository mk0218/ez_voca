# Easy Voca
영어공부하다가 단어 책이 무거워서 만들기로 했습니다.  
While I was studying English, the vocabulary textbook was very heavy, so I decideded to make this app.  
## 현재 상태 | Project status
모델이랑 싸바싸바 하는 중  
## 실행 환경 | Environment
- docker compose (recommended) or local postgresql
- Ubuntu 18.04 or above
- Python 3.8 or above
- Pipenv
## 실행하기 | Running
```
$ docker-compose up -d
$ cd ez_voca_app
$ pipenv run uvicorn app.main:app
```
## 테스트 | Test
[127.0.0.1:8000/docs](127.0.0.1:8000/docs) 또는 
[127.0.0.1:8000/redoc](127.0.0.1:8000/redoc) 으로 접속