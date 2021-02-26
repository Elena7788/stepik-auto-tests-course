import math

from selenium import webdriver
import time


def test_alert_accept():
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()

    browser.get(link)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = int(browser.find_element_by_id('input_value').text)
    result = str(math.log(abs(12 * math.sin(x))))
    browser.find_element_by_id('answer').send_keys(result)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()


    time.sleep(10)

    browser.quit()


def test_switch_to_new_window():
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()

    browser.get(link)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element_by_id('input_value').text)
    result = str(math.log(abs(12 * math.sin(x))))
    browser.find_element_by_id('answer').send_keys(result)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(10)

    browser.quit()
