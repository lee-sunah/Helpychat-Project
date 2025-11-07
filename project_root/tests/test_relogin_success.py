import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage


# 재로그인 테스트
def test_ACCT008_relogin_success(driver):
    wait = WebDriverWait(driver, 10)

    # 로그인
    login_page = LoginPage(driver)
    login_page.page_open()
    login_page.login()
    time.sleep(5)
    assert "qaproject.elice.io" in driver.current_url, "[FAIL] 로그인 실패"
    print("✅ [PASS] 로그인 성공")

    # 로그아웃
    profile = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.MuiAvatar-root"))
    )
    profile.click()

    logout_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='로그아웃']"))
    )
    logout_button.click()

    time.sleep(3)
    assert "accounts" in driver.current_url.lower(), "[FAIL] 로그아웃 실패"
    print("✅ [PASS] 로그아웃 성공")

    # 이메일 연동된 상태에서 비밀번호만 입력하여 재로그인
    login_page.enter_password(login_page.config["login_pw"])
    login_page.click_login_button()

    time.sleep(5)
    assert "qaproject.elice.io" in driver.current_url, "[FAIL] 재로그인 실패"
    print("✅ [PASS] 재로그인 성공")
