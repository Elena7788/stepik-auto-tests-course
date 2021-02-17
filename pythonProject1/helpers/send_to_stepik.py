import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


def send_to_stepik_answer(task_link, answer):
  chrome_options = Options()
  chrome_options.add_argument("--user-data-dir=chrome-data")
  browser = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)

  browser.get(task_link)
  browser.implicitly_wait(4)

  # Проскроллить страницу до элемента с формой
  # browser.execute_script('return arguments[0].scrollIntoView(true);', browser.find_element_by_css_selector('.attempt-main.ember-view'))
  element = browser.find_element_by_css_selector('.attempt-main.ember-view')
  element.location_once_scrolled_into_view
  time.sleep(2)
  browser.find_element_by_css_selector('textarea.textarea.ember-auto-resize.ember-view').send_keys(answer)
  print('Answ = ', answer)
  time.sleep(5)
  browser.find_element_by_css_selector('button.submit-submission').click()
  # button = browser.find_element_by_css_selector('button.submit-submission')
  # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  # button.click()
  time.sleep(20)

  #Для вставки в файл с тестом для ответа на степике, поиск числа во всплывающем окне - последние цифры до двоеточия
  #alert = browser.switch_to.alert
  #alert_text = alert.text
  #alert.accept()
  #answer = alert_text.split(': ')[-1]
