import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from source.PageObject.edit_pim import Pim_add

@pytest.fixture
def setup():
    service = Service(executable_path="C:\\Users\\Nandhu\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_edit(setup):

    obj = Pim_add(setup)
    obj.login_page("Admin","admin123")
    obj.pim_search_btn("James","0275")
    obj.edit_emply("Lia")