import math, time, pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(2)
    browser.quit()


@pytest.mark.parametrize('ending', ['895', '896', '897', '898', '899', '903', '904', '905'])
class TestField:
    def test_filling_fields_different_pages(self, browser, ending):
        link = f"https://stepik.org/lesson/236{ending}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector('.textarea').send_keys(str(math.log(int(time.time()))))

        browser.find_element_by_css_selector('.submit-submission').click()
        time.sleep(5)

        correct_text = browser.find_element_by_tag_name("pre").text

        assert correct_text == "Correct!"

        # The owls are not what they seem! OvO








