from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Pim_add():
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)



    def login_page(self, username, pswrd):
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_field.send_keys(username)
            pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            pswrd_field.send_keys(pswrd)
            button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            button.click()

    def pim_search_btn(self, fname,id):
        try:
            pim_module = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")))
            pim_module.click()
            firstname = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First name']")))
            firstname.send_keys(fname)
            employee_id = self.driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
            employee_id.send_keys(id)
            search = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")))
            search.click()
        except TimeoutException as e:
            print(e)


    def edit_emply(self,lastname):
        try:
            edit_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[contains(text(),'James')])[1]")))
            edit_btn.click()

            lname = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Last Name']")))
            lname.clear()
            lname.send_keys(lastname)
            other_id = self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input")))
            other_id.send_keys("9842")
            save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@type='submit'][normalize-space()='Save'])[1]")))
            save_button.click()
            employee_list = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]")))
            if employee_list.is_displayed():
               print("Employee details edited")
        except NoSuchElementException as e:
            print(e)



