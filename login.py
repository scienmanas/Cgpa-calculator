from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Login() :
    def __init__(self,user,passw) -> None:
        self.user_id = user
        self.password = passw
        
    def PerformLogin(self,driver) :
        # For student login Page
        to_login = driver.find_element(By.CSS_SELECTOR,"#ssubmit")
        to_login.send_keys(Keys.ENTER)
        
        # Performing Login
        user_creden = driver.find_element(By.NAME,"txt_luserid")
        user_creden.send_keys(self.user_id)
        pass_creden = driver.find_element(By.NAME, "txt_lpwd")
        pass_creden.send_keys(self.password)
        login_button = driver.find_element(By.CSS_SELECTOR,"#submit")
        login_button.send_keys(Keys.ENTER)