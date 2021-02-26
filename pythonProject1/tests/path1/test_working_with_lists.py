from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def test_select_when_all_options_hidden_in_dropdown_menu():
    link = 'http://suninjuly.github.io/selects1.html'

    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id('num1').text)
    y = int(browser.find_element_by_id('num2').text)
    answer = str(x + y)

    Select(browser.find_element_by_tag_name("select")).select_by_visible_text(answer)

    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(20)

    browser.quit()


def test_select_when_all_or_part_options_visible_in_dropdown_menu():
    link = 'http://suninjuly.github.io/selects2.html'

    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id('num1').text)
    y = int(browser.find_element_by_id('num2').text)
    answer = str(x + y)

    Select(browser.find_element_by_tag_name("select")).select_by_visible_text(answer)

    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(20)

    browser.quit()
