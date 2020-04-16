import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_in_multilanguage_environment(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_class_name('btn-add-to-basket'), "Submit button not found"
