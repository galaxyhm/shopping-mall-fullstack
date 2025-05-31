# 더 세밀한 paths 설정 예시

# 1. Django 코드만 감지
paths:
  - 'shoppingmall/**/*.py'
  - 'shoppingmall/**/templates/**'
  - 'shoppingmall/**/static/**'
  - 'Dockerfile'

# 2. 특정 파일 제외
paths:
  - 'shoppingmall/**'
  - 'Dockerfile'
  - '!shoppingmall/**/__pycache__/**'
  - '!shoppingmall/**/*.pyc'

# 3. 문서 파일 제외
paths:
  - '**'
  - '!README.md'
  - '!*.md'
  - '!docs/**'
