import time
from src.pages.login_page import LoginPage


def test_ACCT006_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.page_open()

    # 잘못된 비밀번호 입력
    wrong_password = "team2elice!"

    login_page.enter_email(login_page.config["login_id"])
    login_page.enter_password(wrong_password)
    login_page.click_login_button()

    time.sleep(5)

    current_url = driver.current_url
    assert "accounts" in current_url.lower(), "[FAIL] 예상대로 로그인 페이지 유지X"
    print("⛔ [FAIL] 로그인 실패 - 이메일 혹은 비밀번호 불일치")