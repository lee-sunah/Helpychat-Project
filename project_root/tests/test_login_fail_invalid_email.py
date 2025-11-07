import time
from src.pages.login_page import LoginPage


def test_ACCT004_invalid_email(driver):
    login_page = LoginPage(driver)
    login_page.page_open()

    # 잘못된 이메일 입력
    wrong_email = "team1@elice.com"

    login_page.enter_email(wrong_email)
    login_page.enter_password(login_page.config["login_pw"])
    login_page.click_login_button()

    time.sleep(5)

    current_url = driver.current_url
    assert "accounts" in current_url.lower(), "[FAIL] 예상대로 로그인 페이지 유지X"
    print("⛔ [FAIL] 로그인 실패 - 이메일 혹은 비밀번호 불일치")