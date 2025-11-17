import allure
from datetime import datetime

# 스크린샷 찍는 코드
def attach_screenshot(driver, name="screenshot"):
    allure.attach(
        driver.get_screenshot_aspng(),
        name=f"{name}{datetime.now().strftime('%H-%M-%S')}",
        attachment_type=allure.attachment_type.PNG
    )