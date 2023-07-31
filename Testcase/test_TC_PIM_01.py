import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from source.PageObject.Pim_add_employee import Pim_add


@pytest.fixture
def setup():
    service = Service(executable_path="C:\\Users\\Nandhu\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()


def test_add(setup):
    obj = Pim_add(setup)
    obj.login("Admin","admin123")
    obj.pim_add_new_employee_save("James","Charlotte")
    obj.search_edit()