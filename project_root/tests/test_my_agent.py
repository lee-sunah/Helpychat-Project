import time
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage
from src.pages.agent_enter_page import AgentEnterPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

def test_CSTM021_my_agent(driver,login) :

    # 에이전트 페이지 접속
    agent_page = AgentEnterPage(driver)
    agent_page.open()

    my_agent_btn = driver.find_element(By.LINK_TEXT, "내 에이전트")
    my_agent_btn.click()
    time.sleep(3)

    



