# BeanBrief

BeanBrief는 커피 원두 정보를 공유하고 리뷰할 수 있는 커뮤니티 플랫폼입니다.

## 데모 사이트

현재 구현된 사이트는 다음 URL에서 확인하실 수 있습니다:
http://www.beanbrief.duckdns.org/

## 주요 기능

- 커피 원두 목록 조회
- 원두 상세 정보 확인
- 원두 리뷰 작성 및 조회
- 사용자 인증 (로그인/회원가입)

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