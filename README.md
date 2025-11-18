# 🧠 HelpyChat QA Automation Project

## 🛠️ 기술 스택

| 분류 | 기술 / 도구 |
|------|-------------|
| **Testing** | [![Python](https://img.shields.io/badge/python-3.10+-blue)](#), [![Pytest](https://img.shields.io/badge/pytest-automation-green)](#), [![Selenium](https://img.shields.io/badge/selenium-automation-green)](#), Pytest-xdist, Pytest-rerunfailures, [![Allure](https://img.shields.io/badge/report-allure-important)](#) |
| **DevOps** | [![Jenkins](https://img.shields.io/badge/jenkins-ci-orange)](#), [![Docker](https://img.shields.io/badge/docker-container-blue)](#), GitLab, Webhook, Allure Jenkins Plugin |



[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](#)
[![Selenium](https://img.shields.io/badge/selenium-automation-green)](#)
[![Allure](https://img.shields.io/badge/report-allure-important)](#)

---

## 🚀 프로젝트 개요

HelpyChat QA 자동화 프로젝트는 HelpyChat의 주요 기능을 자동화 테스트로 검증하여  
서비스 품질을 향상시키고, CI/CD 환경에서 **안정적인 테스트 자동화 프로세스**를 확립하는 것을 목표로 합니다.

- Pytest + Selenium 기반 UI 자동화
- Jenkins + Docker 기반 파이프라인
- Allure Report로 테스트 가시성 강화
- 구글시트 기반 테스트케이스 관리

---

## 📘 HelpyChat 서비스 소개 (요약)

<details>
<summary><strong>📌 클릭하여 HelpyChat 서비스 설명 펼치기</strong></summary>

### HelpyChat은 기업용 통합 AI 플랫폼으로,
GPT·Claude·Helpy Pro 등 다양한 AI 모델과 기능을 한 곳에서 제공하는 **All-in-One AI 업무 도구**입니다.

### 🔑 핵심 특징
- **통합 플랫폼**: 채팅, 파일 분석, 이미지 생성, PPT 자동 생성 등 여러 AI 기능을 하나의 서비스에서 제공
- **CSAP 기반 보안**: 기업 사용자 대상 강력한 보안 체계
- **크레딧 기반 과금**: 명확한 AI 사용량 관리
- **교육 지원 기능**: K12 문서 생성 등 실무/교육 기능 제공

---

## 🧩 주요 기능 요약

### 1️⃣ 계정 / 조직
- 엘리스 SSO  
- 계정 권한 (기관소유자/관리자/교육자/일반유저)  
- 구성원 초대 및 조직 관리  

### 2️⃣ 빌링
- 크레딧 충전 / 자동 충전  
- 결제 수단 관리  
- 이용 내역 리포트  

### 3️⃣ 채팅
- 실시간 멀티모달 AI 채팅  
- 히스토리 검색/조회  
- 메시지 좋아요/싫어요, 피드백  

### 4️⃣ 고급 기능
- 파일 분석  
- 심층 조사  
- PPT 생성  
- 퀴즈 생성  
- 이미지 생성 및 편집  
- 차트/그래프 생성  

### 5️⃣ 커스텀 에이전트
- 생성/수정/삭제  
- 규칙·역할·기능 설정  
- 공개 범위 설정  

</details>

---

## 🎯 QA 자동화 목표

1. **테스트 자동화 효율화** — 반복 테스트 최소화  
2. **결함 조기 발견** — 기능 전반의 문제점 선제 탐지  
3. **품질 기준 강화** — 사용자 중심의 기능 품질 향상  
4. **자동 리포트** — Allure 기반 결과 시각화  
5. **CI/CD 통합** — Jenkins/Docker 기반 자동화 흐름 구축  

---

## 🧪 테스트 대상 기능

- 로그인/계정 관리  
- 채팅 기능(기본/고급)  
- 파일 분석 및 AI 생성 기능  
- 커스텀 에이전트 기능  
- 빌링 및 결제 흐름  
- UI 요소 및 사용자 플로우  
- 권한별 접근 제어  

---

## 🧩 테스트 설계 기준

| 유형 | 설명 |
|------|------|
| 기능 테스트 | 각 기능 정상 동작 검증 |
| 예외 테스트 | 비정상 입력/오류 플로우 검증 |
| UI 테스트 | 버튼/메뉴/피드백 메시지 확인 |
| 보안 테스트 | 인증·권한·접근제어 검증 |
| 성능 테스트 | 파일 업로드, 대용량 처리 |
| 자동화 테스트 | 반복 기능 자동 검증 |

---

## 🔧 기술 스택

| 분류 | 기술 / 도구 | 설명 |
|------|--------------|-------|
| **Testing** | Python 3.x | 테스트 스크립트 작성 |
| | Pytest | 테스트 프레임워크 |
| | Selenium WebDriver | UI 자동화 |
| | Pytest-xdist | 병렬 실행으로 성능 개선 |
| | Pytest-rerunfailures | Flaky 테스트 자동 재시도 |
| | Allure Report | 시각화된 테스트 결과 |
| **DevOps** | Jenkins | CI 파이프라인 |
| | Docker | 테스트 환경 표준화 |
| | Allure Jenkins Plugin | 리포트 자동 생성 |
| | GitLab | 버전 관리 |
| | Webhook | 자동 실행 트리거 |

---

## 📂 프로젝트 폴더 구조
project_root/
├── tests/
│ ├── login/
│ ├── chat/
│ └── admin/
├── pages/
├── utils/
├── conftest.py
├── Jenkinsfile
└── requirements.txt


---

## 🚨 트러블슈팅 기록

- 병렬 실행 시 WebDriver 충돌 → 워커별 세션 분리  
- 테스트 속도 문제 → xdist + headless 적용  
- Flaky 테스트 발생 → rerunfailures로 안정화  
- Allure 결과 생성 오류 → 경로 초기화/정리 로직 수정  
- CI 환경에서 WebDriver 버전 불일치 → Docker 이미지 내부 버전 고정  

---

## 🌟 프로젝트 차별점

- **Jenkins + Docker** 기반 일관된 테스트 환경 구축  
- **Allure Report**로 한눈에 보는 리포트 제공  
- 병렬 실행으로 **테스트 시간 40~60% 단축**  
- Google Sheets × Pytest 연동으로 테스트 관리 효율 상승  
- QA 자동화를 통해 반복 업무 절감 및 품질 안정화  

---

## 📈 테스트 결과 요약

- 전체 테스트케이스: **XX개**  
- 자동화 적용: **XX개 (커버리지 XX%)**  
- 평균 실행 시간: **XX → XX분 (병렬 적용 후)**  
- 파이프라인 성공률: **XX%**  
- 발견된 주요 이슈: **XX건**  

