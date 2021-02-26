import selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_first():
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.get(link)

    try:
        button = browser.find_element(By.ID, "submit_button")
        button.click()
    finally:
        browser.quit()


def test_second():
    link = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_name('first_name')
        input1.send_keys('Elena')
        input2 = browser.find_element_by_name('last_name')
        input2.send_keys('Sheremet')
        input3 = browser.find_element_by_class_name('city')
        input3.send_keys('Dnipro')
        input4 = browser.find_element_by_id('country')
        input4.send_keys('Ukraine')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла

def test_third():
    link = "http://suninjuly.github.io/find_xpath_form"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_name('first_name')
        input1.send_keys('Elena')
        input2 = browser.find_element_by_name('last_name')
        input2.send_keys('Sheremet')
        input3 = browser.find_element_by_class_name('city')
        input3.send_keys('Dnipro')
        input4 = browser.find_element_by_id('country')
        input4.send_keys('Ukraine')
        button = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()





