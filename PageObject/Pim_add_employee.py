from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Pim_add():
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.actions = ActionChains(self.driver)
        self.username_Name = "username"
        self.password_Name = "password"
        self.login_btn = "button[type='submit']"  # CSS

    def login(self, username, password):
        try:
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, self.username_Name)))
            username_field.send_keys(username)

            pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, self.password_Name)))
            pswrd_field.send_keys(password)

            button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_btn)))
            button.click()

        except TimeoutException as e:
            print(e)



    def pim_add_new_employee_save(self, name, lastname):
        try:
            pim_module = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")))
            pim_module.click()
            add_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")))
            add_btn.click()
            firstname = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First name']")))
            firstname.send_keys(name)
            lname = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Last Name']")))
            lname.send_keys(lastname)
            save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")))
            save_btn.click()
            employee_list = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]")))
            if employee_list.is_displayed():
                print("New Employee Added")
        except TimeoutException as e:
            print(e)

    def search_edit(self):
      try:
          nick_name = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")))
          nick_name.send_keys("Alia")
          other_id = self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input")))
          other_id.send_keys("9842")
          Expiry_Date = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")))
          Expiry_Date.send_keys("2027-07-23")
          SSN_number = self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input")))
          SSN_number.send_keys("4567")
          SIN_number = self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input")))
          SIN_number.send_keys("4789")

          smoker_checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[@class='oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input'])[1]")))
          smoker_checkbox.click()

          service_box = self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input")
          service_box.send_keys("No")
          gender = self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]")))
          gender.click()
          save_new = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button")))
          save_new.click()
          employee_list = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]")))
          if employee_list.is_displayed():
              print("New Employee personal details added Successful")
          # save_success = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="oxd-toaster_1"]')))
          # if save_success.is_displayed():
          #     print("Personal details saved Successfully!!")

      except TimeoutException as e:
          print(e)







        #     self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i")))
        #     nationality = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Algerian')]")))
        #     nationality.click()
        #     print(len(nationality))
        #     self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'American')]"))).click()
        #     Marital_status = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]")))
        #     self.actions.click(Marital_status).perform()
        #
        # except TimeoutException as e:
        #     print(e)



