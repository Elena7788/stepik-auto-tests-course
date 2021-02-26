import unittest, time
from selenium import webdriver


class TestRegistration(unittest.TestCase):
    def test_registration_first(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # required_fields = browser.find_elements_by_css_selector('input:required')
        # for required_field in required_fields:
        # required_field.send_keys('Elena')

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

        self.assertEqual(welcome_text_elt.text, welcome_text, "Congratulations! You have successfully registered!")

        time.sleep(10)

        browser.quit()

    def test_registration_second(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # required_fields = browser.find_elements_by_css_selector('input:required')
        # for required_field in required_fields:
        # required_field.send_keys('Elena')

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

        self.assertEqual(welcome_text_elt.text, welcome_text, "Congratulations! You have successfully registered!")
        time.sleep(10)

        browser.quit()


if __name__ == "__main__":
    unittest.main()
