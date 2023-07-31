import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from source.PageObject.Login_page import LoginPage

@pytest.fixture
def setup():
    service = Service(executable_path="C:\\Users\\Nandhu\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()

def  test_valid_login_page(setup):
     obj = LoginPage(setup)
     obj.valid_login("Admin","admin123")
     if obj.get_login_url() != obj.get_current_url():
         print("Login Successfull!!")
def test_valid_login(setup):
    obj1 = LoginPage(setup)
    obj1.valid_login("Admin", "admin123") #username as "admin"
    if obj1.get_login_url() != obj1.get_current_url():
        print("Login Successfull!!")
