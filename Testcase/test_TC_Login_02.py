import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from source.PageObject.Login_page import LoginPage

@pytest.fixture
def setup():
    service = Service(executable_path="C:\\Users\\Nandhu\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_invalid_username_and_password(setup):

    login = LoginPage(setup)
    login.valid_login("aderet","dd1245")
    if login.get_current_url() == login.get_login_url():
        print("Invalid credentials!!")



def test_invalid_username_with_valid_password(setup):
    login = LoginPage(setup)
    login.valid_login("aderet","admin123")
    if login.get_current_url() == login.get_login_url():
        print("Invalid Credentials!!")


def test_valid_username_with_invalid_password(setup):
    login = LoginPage(setup)
    login.valid_login("Admin","ad$5123")

    if login.get_current_url() == login.get_login_url():
        print("Invalid credentials!!")


def test_empty_username_with_valid_password(setup):
    login = LoginPage(setup)
    login.valid_login("","admin123")

    if login.get_current_url() == login.get_login_url():
        print("Username required!!")


def test_empty_username_with_empty_password(setup):
    login = LoginPage(setup)
    login.valid_login("","")

    if login.get_current_url() == login.get_login_url():
        print("Username and Password required!!")


def test_valid_username_with_empty_password(setup):
    login = LoginPage(setup)
    login.valid_login("Admin","")
    if login.get_current_url() == login.get_login_url():
        print("Password required!!")