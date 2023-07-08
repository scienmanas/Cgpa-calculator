from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from id_and_pass import user_id,passw
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
from grade_system import grade
from tkinter import Tk, messagebox


data_df = pd.read_csv(r"cgpa-calculator\data.csv")
Cgpa = 0.0
Total_Credits = 0
Total_Points = 0

def Display():
    window = Tk()
    window.withdraw()
    window.attributes('-topmost', True)
    messagebox.showinfo(title="Your Cgpa", message=f"Your calculated Cgpa is : {Cgpa}")
    driver.quit()

def CalculateCgpa():
    global Cgpa
    Cgpa = Total_Points/Total_Credits

def GetAndProcessData():
    global Total_Credits
    global Total_Points
    table = driver.find_element(By.CLASS_NAME,"table")
    rows = table.find_elements(By.TAG_NAME,"tr")
    skipable = 0
    for row in rows:
        if skipable < 2 :
            skipable +=1
            continue
        columns = row.find_elements(By.TAG_NAME,"td")
        course = columns[1].text
        grade_achieved = columns[3].text
        if grade_achieved == 'P' :
            continue
        elif grade_achieved == 'I' :
            continue
        credit = int(data_df.Credits[data_df.Code == course])
        Total_Credits += credit
        Total_Points += credit*(grade.get(grade_achieved))

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.get("https://iittp.plumerp.co.in/prod/iittirupati/")
student_login = driver.find_element(By.CSS_SELECTOR,"#ssubmit")
student_login.send_keys(Keys.ENTER)


en_user_id = driver.find_element(By.NAME,"txt_luserid")
en_user_id.send_keys(user_id)

en_pass = driver.find_element(By.NAME, "txt_lpwd")
en_pass.send_keys(passw)

login_button = driver.find_element(By.CSS_SELECTOR,"#submit")
login_button.send_keys(Keys.ENTER)

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

for i in range(8):
    sem_list = driver.find_element(By.ID,"sem")
    select = Select(sem_list)
    select.select_by_index(i)
    proceed_button = driver.find_element(By.ID,"xsubmit")
    proceed_button.click()
    GetAndProcessData()
    
CalculateCgpa()
Display()