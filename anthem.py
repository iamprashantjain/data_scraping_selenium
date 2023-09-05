from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service	
import time
import pyautogui
from bs4 import BeautifulSoup
import pdb
import pandas as pd



# Set up WebDriver
s = Service(r"C:\Users\iampr\Downloads\Compressed\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Open URL
url = "https://findcare.anthem.com/search-providers"
driver.get(url)
time.sleep(10)


element = driver.find_element(By.XPATH, "//a[contains(text(), 'Basic search as a guest')]")
element.click()


dropdown = Select(driver.find_element(By.NAME, 'medical_plan_network'))
dropdown.select_by_visible_text("Medical Plan or Network (may also include dental, vision, or pharmacy benefits)")

# "Medical Plan or Network (may also include dental, vision, or pharmacy benefits)"