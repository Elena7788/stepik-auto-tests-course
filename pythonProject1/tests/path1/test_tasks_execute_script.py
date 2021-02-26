import time

from selenium import webdriver

import math


def test_wrong_task_scroll_it():
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # or browser.execute_script("window.scrollBy(0, 100);")

    # or for Console: // javascript
    # button = document.getElementsByTagName("button")[0];
    # button.scrollIntoView(true)

    button.click()
    assert True


def test_task_js_execute_script_scroll_it():
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element_by_id('input_value').text)
    result = str(math.log(abs(12 * math.sin(x))))

    browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element_by_id('answer').send_keys(result)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(20)

    browser.quit()


