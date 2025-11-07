import time
from src.pages.login_page import LoginPage


def test_ACCT003_invalid_email_domain(driver):
    login_page = LoginPage(driver)
    login_page.page_open()

    # 잘못된 이메일 입력(도메인X)
    wrong_email = "team2"

    login_page.enter_email(wrong_email)
    login_page.enter_password(login_page.config["login_pw"])
    login_page.click_login_button()

    time.sleep(5)

    current_url = driver.current_url
    assert "accounts" in current_url.lower(), "[FAIL] 예상대로 로그인 페이지 유지X"
    print("⛔ [FAIL] 로그인 실패 - 이메일 도메인 불일치")