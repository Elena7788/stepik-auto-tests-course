import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_different_interface_languages(browser):
    browser.get(link)
    time.sleep(30)
    button_add_to_basket = browser.find_element_by_css_selector("#add_to_basket_form")

    assert button_add_to_basket.is_displayed()

