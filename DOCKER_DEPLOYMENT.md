# GitHub Secrets 설정 가이드

GitHub 저장소에서 다음 secrets를 설정해야 합니다:

## 필수 Secrets

1. **HARBOR_REGISTRY**: Harbor 레지스트리 URL (예: harbor.example.com)
2. **HARBOR_USERNAME**: Harbor 레지스트리 사용자명
3. **HARBOR_PASSWORD**: Harbor 레지스트리 비밀번호 또는 토큰
4. **HARBOR_PROJECT**: Harbor 프로젝트 이름 (예: my-project)

## Secrets 설정 방법

1. GitHub 저장소 페이지로 이동
2. Settings → Secrets and variables → Actions
3. "New repository secret" 클릭
4. 위의 secrets 추가

## 환경 변수 설정

이제 모든 민감한 정보가 GitHub Secrets로 관리됩니다:

- `HARBOR_REGISTRY`: Harbor 레지스트리 URL
- `HARBOR_USERNAME`: Harbor 사용자명  
- `HARBOR_PASSWORD`: Harbor 비밀번호/토큰
- `HARBOR_PROJECT`: Harbor 프로젝트 이름

워크플로우 파일에서 수정 가능한 값:
- `IMAGE_NAME`: Docker 이미지 이름 (현재: shoppingmall-django)

## 트리거 조건

현재 워크플로우는 다음 경우에 실행됩니다:
- main 또는 develop 브랜치에 push
- v*로 시작하는 태그 push (예: v1.0.0)
- main 브랜치로의 pull request

## 이미지 태그 규칙

- 브랜치명 (예: main, develop)
- PR 번호 (예: pr-123)
- 시멘틱 버전 (예: v1.0.0, v1.0, v1)
- 브랜치-SHA (예: main-abc123f)
