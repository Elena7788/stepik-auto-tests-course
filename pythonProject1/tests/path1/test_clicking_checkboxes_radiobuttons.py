from selenium import webdriver
import time
import math



def test_captcha_for_robots():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = 'http://suninjuly.github.io/math.html'

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(20)

    browser.quit()


def test_find_radiobutton_checked():
    link = 'http://suninjuly.github.io/math.html'

    browser = webdriver.Chrome()
    browser.get(link)

    # проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element_by_id('peopleRule')
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    # or assert people_checked == "true", "People radio is not selected by default"

    # проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    # проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

    # проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None

    # закрываем браузер после всех манипуляций
    browser.quit()


def test_finding_treasure_with_get_attribute():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = 'http://suninjuly.github.io/get_attribute.html'

    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(20)

    browser.quit()