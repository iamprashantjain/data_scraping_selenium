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
import pdb
from selenium.webdriver.common.action_chains import ActionChains


# Set up WebDriver
s = Service(r"C:\Users\iampr\Downloads\Compressed\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Open URL
url = "https://connect.werally.com/behavioralProvider/rootLocation"
driver.get(url)
time.sleep(15)


continue_btn = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[1]/div/chrome/div/div/div[2]/div/a")
continue_btn.click()
time.sleep(15)


find_provider = driver.find_element(By.XPATH,"/html/body/main/div[4]/div/section/div/div/div[1]/div/div/div[2]/div[1]/a")
actions = ActionChains(driver)
actions.double_click(find_provider).perform()
time.sleep(15)

updated_url = driver.current_url
driver.get(updated_url)
driver.refresh()
time.sleep(15)

behavorial_directory = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[1]/div/chrome/div/div/div[2]/ul/li[2]/button/plan-guided-search-node/div[2]/div[1]")
behavorial_directory.click()
time.sleep(15)

medicaid_plans = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[1]/div/chrome/div/div/div[2]/ul/li[4]/button/plan-guided-search-node/div[2]/div[1]")
medicaid_plans.click()
time.sleep(15)

washingtn = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[1]/div/chrome/div/div/state-listing-selection/div/div/ul/li[29]/a/div")
washingtn.click()
time.sleep(15)


imc = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[1]/div/chrome/div/div/state-plan-selection/div/div/ul/li[4]/button/div")
imc.click()
time.sleep(15)


people = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[1]/div/chrome/div/content-hopper/div[1]/div/div/div[4]/div[1]/ul/li[1]/guided-search-link/button/div[2]/div[1]")
people.click()
time.sleep(15)


area_expertise = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[1]/div/chrome/div/content-hopper/div[1]/div/div/div[3]/div[1]/ul/li[3]/guided-search-link/button/div[2]/div")
area_expertise.click()
time.sleep(15)


G = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[1]/div/chrome/div/content-hopper/div[1]/div/div/div[3]/div[1]/guided-search-list/div[2]/div[1]/button[7]")
G.click()
time.sleep(15)


general_therapy = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[1]/div/chrome/div/content-hopper/div[1]/div/div/div[3]/div[1]/guided-search-list/ul/li[1]/h2/button")
general_therapy.click()
time.sleep(15)


chng_location = driver.find_element(By.XPATH,"/html/body/div[3]/div/main/div[1]/div/chrome/div/div/guided-search-results-header/div/div[7]/div[1]/div/change-location/div/button/p[2]")
chng_location.click()
time.sleep(15)



enter_box = driver.find_element(By.XPATH,"/html/body/div[9]/div/div/div/div/div[2]/div[2]/input")
enter_box.send_keys("Seattle, WA")


update_location = driver.find_element(By.XPATH,"/html/body/div[9]/div/div/div/div/div[2]/div[3]/button[1]")
update_location.click()
time.sleep(15)