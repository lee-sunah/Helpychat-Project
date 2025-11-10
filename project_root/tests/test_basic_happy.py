import time 
import pytest 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from src.pages.login_page import LoginPage 
from src.pages.agent_page import AgentPage 


# --- 필수값으로만 에이전트 생성(이름,규칙) --- 
def test_CSTM005_with_essential_field(new_agent): 
    # 1.로그인 
    # 2. AgentPage 객체 생성 / 에이전트 생성 페이지 이동 

    # 3. 필수값 이름/규칙 입력 
    new_agent.set_name("테스트") 
    new_agent.set_rules("테스트") 
    time.sleep(2)

    # 4. 강제로 동적요소 업데이트
    new_agent.refresh()
    time.sleep(5)

    # 5. 자동 저장, 만들기 버튼 활성화될 때까지 대기 
    new_agent.wait_for_save() 
    new_agent.wait_for_button() 
    
    # 6. 만들기 클릭
    new_agent.click_create(), "[FAIL] 만들기 버튼 활성화X" 

    # 7. 공개 설정 후 저장 클릭
    new_agent.click_save()

    # 8. 에이전트 생성 메세지 확인
    text = new_agent.driver.find_element(By.ID, "notistack-snackbar").text.strip()

    assert "에이전트가 생성 되었습니다." in text, "[FAIL] 생성 실패"
    print("✅ [PASS] 에이전트 생성 완료") 
    time.sleep(5)




