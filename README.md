# 🧠 AI HelpyChat QA Project!

> HelpyChat QA 프로젝트는 HelpyChat 서비스의 **핵심 기능 품질을 보증(QA)** 하고  
> **테스트 자동화 기반 CI/CD 프로세스 구축**을 목표로 합니다.  
> 본 프로젝트는 HelpyChat의 다양한 기능 —  
> **계정/조직 관리, 빌링, 채팅, 파일 분석, AI 생성 기능, 커스텀 에이전트 등**을 대상으로  
> 테스트 케이스(TC)를 설계하고, 자동화 스크립트(Pytest + Selenium 등)로 검증을 수행합니다.


##  🎯 프로젝트 목표

| 핵심 가치 | 설명 |
|------------|------|
|  **효율성 향상** | QA 자동화를 통해 반복 테스트를 최소화 |
| **품질 향상** | 사용자 중심 테스트로 제품 신뢰도 강화 |
| **효율적 리포트** | 테스트 결과 자동 리포트 및 로그 관리 |
| **CI/CD 지원** | 지속적 통합/배포 환경에서 테스트 자동화 수행   |


## 🧩 테스트 대상 핵심 기능

<details>
<summary><strong>1️⃣ 계정 / 조직 관련 기능</strong></summary>

- 로그인 / 로그아웃  
- 계정 정보 및 조직 설정 진입  

</details>

<details>
<summary><strong>2️⃣ 빌링 & 이용내역</strong></summary>

- 크레딧 잔량 표시 확인  
- 결제·이용량 화면 진입 여부 검증  

</details>

<details>
<summary><strong>3️⃣ 채팅 히스토리 기능</strong></summary>

- 새 채팅 생성  
- 히스토리 목록 조회 및 검색  
- 에이전트별 대화 필터링  
- 과거 대화 전체 내용 스크롤·노출 확인  

</details>

<details>
<summary><strong>4️⃣ 채팅 기본 기능</strong></summary>

- 텍스트 기반 AI 응답(실시간 대화 흐름)  
- 이미지·문서 등 멀티모달 입력 처리  
- 메시지 상호작용(복사 / 수정 / 좋아요·싫어요)  
- 최신 메시지 자동 스크롤 이동 확인  

</details>

<details>
<summary><strong>5️⃣ 채팅 고급 기능</strong></summary>

- 파일 업로드: 문서·이미지 업로드 후 AI 분석  
- 심층 조사: 특정 주제의 디테일 리서치 결과 검증  
- 구글 검색: 외부 검색 기반 응답 흐름 검증  
- PPT 자동 생성: 입력 기반 슬라이드 생성 여부 확인  
- 퀴즈 자동 생성: 유형·난이도별 생성 흐름 검증  
- 이미지 생성: 프롬프트 기반 시각 이미지 생성  

</details>

<details>
<summary><strong>6️⃣ 맞춤화(커스텀 에이전트) 기능</strong></summary>

- 에이전트 생성 / 조회 / 수정 / 삭제  
- 설정 항목 검증: 이름, 설명, 규칙, 시작 메시지 등  
- 기능 선택 옵션(Web Search, Code Execution 등)  
- 공개 범위 옵션 확인(기관공개 / 나만보기 등)  

</details>

## 🧰 기술 스택

<div align="center">

| 분야 | 도구 |
|------|-----------|
| **Automation** | Python · Selenium · PyTest |
| **CI/CD** | Jenkins Declarative Pipeline |
| **Container** | Docker + Jenkins |
| **Reporting** | Allure Report |
| **Parallel Testing** | pytest-xdist |
| **Rerun** | pytest-rerunfailures |
| **VC** | GitLab |

</div>

## 🔥 트러블슈팅 핵심 요약

### ⚡ 병렬 실행 최적화
- 문제: `pytest -n 2` 실행 시 WebDriver 충돌  
- 원인: fixture가 세션을 공유  
- 해결: **function scope fixture 적용**  
- 성과: 전체 실행 속도 약 **30% 단축**

### ⚡ 테스트 불안정성 → Rerun 적용
- 느린 응답/랜덤 지연 → 테스트 Fail  
- `--reruns 2 --reruns-delay 2` 적용  
- **불안정 테스트 자동 보정**

### ⚡ Jenkins chrome driver 문제 해결
- Chrome preferences 문제 → 자동 다운로드 옵션 수동 설정 
- 해결: Jenkinsfile .. 내용 수정하기

### ⚡ 파일 다운로드 실패 해결
- Chrome 정책으로 다운로드 차단 문제 발생  
- 해결: preferences 수정 → 자동 다운로드 허용  
- Allure 스크린샷을 통해 실패 지점 즉시 확인 가능


## ✨ 프로젝트 차별점

### ⭐ Allure Report
- 테스트 단계별 시각화  
- 실패 시 화면 캡처 자동 첨부  
- Jenkins와 자동 퍼블리시 연동  

### ⭐ Jenkins + Docker 파이프라인
- GitLab Push → 자동 테스트  
- 동일한 환경에서 재현 가능  
- 손쉬운 확장 구성  

### ⭐ 테스트 안정성 & 최적화
- 병렬 실행으로 속도 향상  
- Rerun 기반 Fail 감소  
- 명시적 대기 기반 신뢰도 확보  


## 📊 테스트 결과 요약

| 항목 | 결과 |
|------|------|
| 총 테스트 케이스 | **272개** |
| 자동화 성공 케이스 | **90개** |
| Jenkins 성공률 평균 | **70.97%** |


## 🟩 기능 완료 현황 (Feature Completion Status)

<div align="center">

| 기능 구분 | 완료 현황 | 담당자 |
|----------|-----------|-----------|
| 💬 **채팅 고급 기능** | **19 / 19 (100%)** | 강해리 |
| 💭 **채팅 기본 기능** | **28 / 28 (100%)** | 이선아 |
| 🗂 **채팅 히스토리 기능** | **10 / 10 (100%)** | 최고은 |
| 💳 **빌링 기능** | **1 / 1 (100%)** | 김설아 |
| 👥 **계정·조직 기능** | **12 / 12 (100%)** | 김설아 |
| 🎛 **맞춤화 기능** | **20 / 20 (100%)** | 김설아 & 최고은 |


</div>


## ▶ 실행 방법



