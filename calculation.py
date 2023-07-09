from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
from tkinter import Tk, messagebox
INDEN = "------------------------------------------\n"

class Calculation() :
    def __init__(self,driver) :
        self.grade = {
        'S' : 10,
        'A' : 9,
        'B' : 8,
        'C' : 7,
        'D' : 6,
        'E' : 4,
        'U' : 0,
        'F' : 0,
        'W' : 0,
        'X' : 0,
        'Y' : 0
        }
        self.driver = driver
        self.Cgpa = 0.0
        self.Total_Credits_sem = [] 
        self.Total_Point_sem = []
        self.data_df = pd.read_csv(r"Cgpa-calculator\data.csv")
        
    
    def iterate(self) :
        i = 0
        while True:
            sem_list = self.driver.find_element(By.ID,"sem")
            select = Select(sem_list)
            select.select_by_index(i)
            proceed_button = self.driver.find_element(By.ID,"xsubmit")
            proceed_button.click()
            try : 
                tuple_val = self.GetAndProcessData()
                self.Total_Credits_sem.append(tuple_val[0])
                self.Total_Point_sem.append(tuple_val[1])
            except Exception as E:
                break
            i += 1
                
            
    def GetAndProcessData(self):
        Credits_ = 0
        Points_ = 0
        table = self.driver.find_element(By.CLASS_NAME,"table")
        rows = table.find_elements(By.TAG_NAME,"tr")
        skipable = 0
        for row in rows:
            if len(rows) == 2 :
                return False
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
            credit_of_sub = int(self.data_df.Credits[self.data_df.Code == course])
            Credits_ += credit_of_sub
            Points_ += credit_of_sub*(self.grade.get(grade_achieved))
        return (Credits_,Points_)
    
    def Display(self) :
        self.window = Tk()
        self.window.withdraw()
        self.window.attributes('-topmost', True)
        self.DisplayText ="Your Calculated Gpa/Cgpa are as follows : \n\n"
        for i in range(len(self.Total_Credits_sem)) :
            gpa = self.Total_Point_sem[i]/self.Total_Credits_sem[i]
            self.DisplayText += f"Gpa of {i+1} sem is : {gpa}\n"
        self.DisplayText += INDEN
        Cgpa = sum(self.Total_Point_sem)/sum(self.Total_Credits_sem)
        self.DisplayText += f"Total Cgpa = {Cgpa}\n"
        self.DisplayText += INDEN
        messagebox.showinfo(title=f"Your Grades",message=self.DisplayText)
        
        
            