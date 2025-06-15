# 📘 웹서버 컴퓨팅 AD 프로젝트: BeanBrief

## 🔍 개요
이 프로젝트는 Django 웹 프레임워크를 기반으로 한 **질문 게시판 시스템**입니다. 사용자는 질문을 등록하고, 수정 및 삭제할 수 있으며, 댓글을 달고 파일도 업로드할 수 있습니다. 또한, 교과서의 스크롤 기능과 Markdown기능을 추가했습니다.
---

## 🚀 주요 서비스 기능 (과제 5~9 기반)

###  1. 클래스메서드 (과제 5)
###  2. Request 객체 (과제 6)
###  3. auth 클래스 (과제 7)
###  4. API 응답메세지 (과제 8)
###  5. 서비스/뷰/예외처리 분리 (과제 9)

## 📚 교과서 내용 기반 기능

### 3-13. 스크롤 기능
### 3-14. Markdown기능

## 데모 사이트

현재 구현된 사이트는 다음 URL에서 확인하실 수 있습니다:
http://www.beanbrief.duckdns.org/

## 기술 스택

- Django 5.2.1
- Python
- SQLite
- Bootstrap

## 설치 및 실행 방법

1. 저장소 클론
```bash
git clone https://github.com/UH3135/BeanBrief-AI.git
cd beanbrief-ai
```

2. 가상환경 생성 및 활성화
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 또는
.venv\Scripts\activate  # Windows
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```

4. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

5. 개발 서버 실행
```bash
python manage.py runserver
```

## Kaggle 데이터 로드하기

BeanBrief는 Kaggle의 커피 리뷰 데이터셋을 사용합니다. 데이터를 로드하기 위해서는 다음 단계를 따르세요:

1. Kaggle API 토큰 설정
   - Kaggle 계정 설정에서 API 토큰을 다운로드
   - `.env` 파일에 토큰 정보 추가

2. 데이터 로드 명령어 실행
```bash
python manage.py seed_beans
```

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.
