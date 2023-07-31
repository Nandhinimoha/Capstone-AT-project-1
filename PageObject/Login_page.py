from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        self.username_Name = "username"
        self.password_Name = "password"
        self.login_btn = "button[type='submit']"  # CSS selector

    def get_login_url(self):
        return "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def get_cookie(self):
        Cookie_before = self.driver.get_cookies()[0]["value"]
        return Cookie_before

    def get_current_url(self):
        return self.driver.current_url

    def get_after(self):
        Cookie_after = self.driver.get_cookies()[0]["value"]
        return Cookie_after

    def valid_login(self, username, password):
        try:
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, self.username_Name)))
            username_field.send_keys(username)

            pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, self.password_Name)))
            pswrd_field.send_keys(password)

            button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_btn)))
            button.click()

        except TimeoutException as e:
            print(e)