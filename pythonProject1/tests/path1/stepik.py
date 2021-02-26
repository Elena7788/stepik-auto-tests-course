from selene import have
from selene.support.shared import browser

browser.config.hold_browser_open = True

def test_find_link_text():
    browser.open('http://suninjuly.github.io/find_link_text')
    browser.element('[href="find_link_text_redirect13.html"]').click()

    # Add
    browser.element('[name=first_name]').type('Elena').press_enter()
    browser.element('[name=last_name]').type('Sheremet').press_enter()
    browser.element('.city').type('Dnipro').press_enter()
    browser.element('#country').type('Ukraine').press_enter()

    #browser.quit()




def test_add_huge_form():
    browser.open('http://suninjuly.github.io/huge_form.html')
    elements = browser.all('[type="text"]')

    for element in elements:
        element.send_keys('ok')

    button = browser.element('.btn')
    button.click()
    #browser.quit()

def test_find_xpath_form():
    browser.open('http://suninjuly.github.io/find_xpath_form')


    # Add
    browser.element('[name=first_name]').type('Elena')
    browser.element('[name=last_name]').type('Sheremet')
    browser.element('.city').type('Dnipro')
    browser.element('#country').type('Ukraine')

    button = browser.element('/html/body/div/form/div[6]/button[3]')
    button.click()
   # browser.quit()

def test_registration1_form():
    browser.open('http://suninjuly.github.io/registration1.html')
    browser.element('[class="form-control first"]').type('Elena')
    browser.element('[class="form-control second"]').type('Sheremet')
    browser.element('[class="form-control third"]').type('dnipro@gmail.com')
    button = browser.element('[class="btn btn-default"]')
    button.click()
    

