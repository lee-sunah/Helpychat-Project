import time
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage
from src.pages.agent_enter_page import AgentEnterPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

def test_CSTM030_agent_delete(driver,login) :
    wait = WebDriverWait(driver, 10)

    # 내 에이전트 이동
    agent_page = AgentEnterPage(driver)
    agent_page.open()
    my_agent_btn = driver.find_element(By.LINK_TEXT, "내 에이전트")
    my_agent_btn.click()

    # 에이전트 목록 확인, 첫번째 에이전트 삭제
    agent_list = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='virtuoso-item-list']")))
    first_agent = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-item-index='0'] > a.MuiPaper-root")))

    bin_button = first_agent.find_element(By.CSS_SELECTOR, "svg[data-testid='trashIcon']").click()
    delete_button = driver.find_element(By.XPATH, "//button[text()='삭제']").click()

    # 삭제 메세지
    message = wait.until(EC.presence_of_element_located((By.ID, "notistack-snackbar"))).text.strip()
    assert "에이전트가 삭제되었습니다." in message, "⛔ [FAIL] 삭제 실패"
    print("✅ [PASS] 에이전트 삭제 완료") 


    


