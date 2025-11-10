import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config_reader import read_config


def test_CADV021_deep_investigation_request(driver, login, click_plus, send_test_message):
    """심층 조사 기능 테스트 """

    config = read_config("helpychat")
    base_url = config["base_url"]
    driver.get(base_url)
    wait = WebDriverWait(driver, 15)

    click_plus()

    deep_investigation_btn = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "div.MuiButtonBase-root[role='button'] svg[data-icon='book-open-cover']"
        ))
    )
    driver.execute_script("arguments[0].closest('div[role=\"button\"]').click();", deep_investigation_btn)
    print("✅ 심층 조사 버튼 클릭 완료")

    send_test_message("AI윤리문제에 대해 조사해줘")

    # 시작 버튼 클릭
    start_button = wait.until(
        EC.element_to_be_clickable((
            By.XPATH, "//button[.//span[text()='시작'] or contains(., '시작')]"
        ))
    )
    driver.execute_script("arguments[0].click();", start_button)
    print("▶️ '시작' 버튼 클릭 완료 — 심층조사 진행 중...")

    # 조사 완료 대기 (최대 12분까지 대기)
    try:
        complete_label = WebDriverWait(driver, 720).until(   # 720초 = 12분
            EC.presence_of_element_located((
                By.XPATH, "//span[contains(text(), '조사 완료')]"
            ))
        )
        print("✅ '조사 완료' 문구 감지됨 — 심층조사 성공적으로 종료")
    except:
        print("❌ '조사 완료' 문구를 찾지 못했습니다 (시간 초과)")
        assert False, "'조사 완료' 텍스트가 표시되지 않았습니다."

    # 6️⃣ 최종 검증
    assert "조사 완료" in driver.page_source, "❌ 조사 완료 문구가 화면에 없습니다."
    print("✅ 테스트 성공: '심층 조사' 요청 및 완료 검증 완료")