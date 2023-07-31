import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from source.PageObject.Delete_employee import delete_page


@pytest.fixture
def setup():
    service = Service(executable_path="C:\\Users\\Nandhu\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_delete_module(setup):
    obj = delete_page(setup)
    obj.login_page("Admin","admin123")
    obj.pim_search_btn("James","0275")
    obj.delete_employee()