import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginP:
    email_Id = 'email'
    password_Id = 'pass'
    button_id = 'loginbutton'


    def __init__(self,driver):
        self.driver =driver



    def setusername(self,username):
        self.driver.find_element(By.ID, self.email_Id).send_keys(username)
        time.sleep(2)

    def setpassword(self,passowrd):
        self.driver.find_element(By.ID,self.password_Id).send_keys(passowrd)
        time.sleep(2)


    def clicklogin(self):
        self.driver.find_element(By.ID, self.button_id).click()
        time.sleep(2)





