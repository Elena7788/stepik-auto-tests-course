from selenium import webdriver
import time
import os


def test_registration_first():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        #required_fields = browser.find_elements_by_css_selector('input:required')
        #for required_field in required_fields:
            #required_field.send_keys('Elena')

        input1 = browser.find_element_by_css_selector('.first:required')
        input1.send_keys('Elena')
        input2 = browser.find_element_by_class_name('second:required')
        input2.send_keys('Elenova')
        input3 = browser.find_element_by_class_name('third:required')
        input3.send_keys('elena@gmail.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)


        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text


        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:

        time.sleep(10)

        browser.quit()


def test_registration_second():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        #required_fields = browser.find_elements_by_css_selector('input:required')
        #for required_field in required_fields:
            #required_field.send_keys('Elena')

        input1 = browser.find_element_by_css_selector('.first:required')
        input1.send_keys('Elena')
        input2 = browser.find_element_by_class_name('second:required')
        input2.send_keys('Elenova')
        input3 = browser.find_element_by_class_name('third:required')
        input3.send_keys('elena@gmail.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:

        time.sleep(10)

        browser.quit()


def test_registration_with_file_upload():
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name('firstname').send_keys('Elena')

    browser.find_element_by_name('lastname').send_keys('Elenova')

    browser.find_element_by_name('email').send_keys('elena@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_id('file').send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(10)

    browser.quit()

