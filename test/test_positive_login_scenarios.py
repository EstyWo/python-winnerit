# .\.venv\Scripts\Activate.ps1
# deactivate

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


def test_standard_user_login(browser):
    login_page = LoginPage(browser)

    # Navigation to the app
    login_page.open_home_page()

    # Filling Form
    login_page.type_username("standard_user")
    login_page.type_password('secret_sauce')
    login_page.click_login_button()

    # Validation of redirection
    current_url = browser.current_url
    print(f"{current_url = }")
    assert current_url == "https://www.saucedemo.com/inventory.html"

    products_page_title = browser.find_element(By.XPATH, value='//*[@data-test="title"]').text
    print(f"{products_page_title = }")
    assert products_page_title == "Products"


def test_locked_out_user_login(browser):
    login_page = LoginPage(browser)

    # Navigation to the app
    login_page.open_home_page()

    # Filling Form
    login_page.type_username("locked_out_user")
    login_page.type_password('secret_sauce')
    login_page.click_login_button()

    # Validation of Error message
    error_message_text = browser.find_element(By.CSS_SELECTOR, value='[data-test="error"]').text
    print(f"{error_message_text = }")
    assert error_message_text == "Epic sadface: Sorry, this user has been locked out."
