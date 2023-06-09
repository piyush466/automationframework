import pytest as pytest
from selenium import webdriver
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome(r"C:\Users\ASUS\OneDrive\Desktop\chrome driver\chromedriver_win32 (1)\chromedriver.exe")
    driver.get("https://www.facebook.com/login/")
    return driver
