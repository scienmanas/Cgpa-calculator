from selenium import webdriver
from login import Login
from switchtopath import SwitchPath
from calculation import Calculation

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.get("https://iittp.plumerp.co.in/prod/iittirupati/")

login_ = Login()
login_.PerformLogin(driver)

switch = SwitchPath()
switch.SwitchToGrades(driver)

calculate = Calculation(driver)
calculate.iterate()
calculate.Display()
driver.quit()