from random import randint
from selenium import webdriver
from login import Login
from switchtopath import SwitchPath
from calculation import Calculation
from flask import Flask, render_template, request

route_= ""

app = Flask(__name__)
route_ = ""
user_id = ""
user_password = ""


@app.route('/')
def home():
    global route_
    route_ = str(randint(736437,100000000))
    return render_template('index.html')

@app.route(f'/{route_}', methods=['POST','GET'])
def GetAndProcess():
    global user_id
    global user_password
    user_id = request.form["user_id"]
    user_password = request.form["user_password"]

    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)

    driver = webdriver.Chrome(options=option)
    driver.get("https://iittp.plumerp.co.in/prod/iittirupati/")

    login_ = Login(user_id,user_password)
    login_.PerformLogin(driver)

    switch = SwitchPath()
    switch.SwitchToGrades(driver)

    calculate = Calculation(driver)
    calculate.iterate()
    StudentGradeData = calculate.ReturnCalculatedValues()
    driver.quit()
    route_ = ""
    user_id = ""
    user_password = ""
    return render_template('result.html',data = StudentGradeData)

if __name__ == "__main__":
    app.run(debug=True)




