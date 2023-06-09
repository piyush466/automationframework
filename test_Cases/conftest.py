import pytest as pytest
from selenium import webdriver
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/login/")
    return driver
