from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SwitchPath() :
    def __init__(self) -> None:
        pass
    
    def SwitchToGrades(self,driver):
        lines_frame = driver.find_element(By.ID,"sidef")
        driver.switch_to.frame(lines_frame)

        lines = driver.find_element(By.ID,"polmenu")
        lines.click()

        driver.switch_to.default_content()

        academic_frame = driver.find_element(By.ID,"menuf")
        driver.switch_to.frame(academic_frame)

        academic = driver.find_element(By.ID,"modmenu_Academics")
        academic.click()

        student_grade_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Academics"]/table/tbody/tr[6]/td/div/pbanc')))
        student_grade_button.click()

        driver.switch_to.default_content()

        sem_list_frame = driver.find_element(By.ID,"listf")
        driver.switch_to.frame(sem_list_frame)        

    