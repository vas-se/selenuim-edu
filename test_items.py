import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_in_multilanguage_environment(browser):
    browser.get(link)
    try:
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
        )
    except:
        assert False, "Button not found"
    finally:
        time.sleep(5)
