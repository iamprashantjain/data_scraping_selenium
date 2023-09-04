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
url = "https://findaprovider.coordinatedcarehealth.com/search-results"
driver.get(url)

time.sleep(10)

# Enter location
location = driver.find_element(By.XPATH, "/html/body/div[1]/page-component/search-component/div/div/location-page/main/div/div[2]/div/md-card/location-selection/form/div/div[1]/div[1]/div/input")
location.send_keys("Seattle, WA, USA")
location.send_keys(Keys.ENTER)

time.sleep(10)

# Select plan from dropdown
plan_dropdown = driver.find_element(By.XPATH, "/html/body/div[1]/page-component/search-component/div/div/location-page/main/div/div[2]/div/md-card/location-selection/form/div/div[1]/div[4]/div/div/div/select")
select = Select(plan_dropdown)
select.select_by_visible_text("Coordinated Care Medicaid")
plan_dropdown.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys(Keys.ENTER)
time.sleep(2)

# Click on Behavioral Health category
wait = WebDriverWait(driver, 20)
behavorial_health = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/page-component/search-component/div/div/main-component/main/div[6]/div[2]/div/div[2]/div/md-card/categories-container/div/category-tiles/category-tile-group[1]/div[3]/category-tile/p-standard-component/span")))
behavorial_health.click()
time.sleep(2)


#clicking on professional using image
professional = r"C:\Users\iampr\Desktop\1.png"
professional_location = pyautogui.locateOnScreen(professional)

if professional_location:
    x, y, width, height = professional_location
    center_x = x + width // 2
    center_y = y + height // 2

    pyautogui.click(center_x, center_y)



#clicking on search using image
search_box = r"C:\Users\iampr\Desktop\2.png"
search_box_location = pyautogui.locateOnScreen(search_box)

if search_box_location:
    x, y, width, height = search_box_location
    center_x = x + width // 2
    center_y = y + height // 2

    pyautogui.click(center_x, center_y)



#infinite scrolling
height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(10)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
    height = new_height



#saving complete html
complete_html = driver.page_source


# Save the complete HTML content to a file
with open('acuity_page2.html', 'w', encoding='utf-8') as f:
    f.write(complete_html)



with open('acuity_page.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all provider div elements
provider_divs = soup.find_all("div", class_="row search-result-row")


names_list = []
titles_list = []
specialities_list = []
addresses_list = []
counselors_list = []
accepting_new_patients_list = []


for provider_div in provider_divs:
    
    name_data = provider_div.find('h2', {'class': 'text-left text-20 leading-32 text-theme-black font-normal mb-2 ng-binding'}).text.strip().split(',')
    name = name_data[0]
    title = name_data[1]
    speciality = provider_div.find('span', {'class': 'p-muted'}).text.strip()
    
    address_elements = provider_div.find_all('span', {'_ngcontent-app-id-c9': True, 'ng-if': 'textValue'})
    addr1 = address_elements[0].text.strip()
    addr2 = address_elements[1].text.strip()
    complete_addr = addr1 + "," +  addr2

    span_element = provider_div.find('span', class_='text-transform specialty-item ng-binding ng-scope pl-0')
    counselor = span_element.get_text().strip()
    rearranged_counselor = ' - '.join(reversed(counselor.split('—'))).strip()

    
    sidebar = provider_div.find_all('ul', class_ = 'stoplights')
    for i in sidebar:
        li_element = i.find('li')
        check_mark_div = li_element.find('div', class_='check-mark')
        check_mark_text = check_mark_div.text.strip()
        if check_mark_text == 'Accepting new patients':
            if check_mark_div:
                accepting_new_patients = "Yes"
            else:
                accepting_new_patients = "No"
    
    
    show_details_btn = r"C:\Users\iampr\Desktop\3.png"
    show_details_btn_location = pyautogui.locateOnScreen(show_details_btn)


    if show_details_btn_location:
        x, y, width, height = show_details_btn_location
        center_x = x + width // 2
        center_y = y + height // 2

        pyautogui.click(center_x, center_y)

    expanded_info = driver.find_element(By.ID, "details-expander-27796-expander")
    additional_languages = expanded_info.find_element(By.xpath(".//div[data-cy='languageSpokenInOffice']//p[@class='label-value__value']")).text
    age_limitations = expanded_info.find_element(By.xpath(".//div[data-cy='Age Limitations']//p[@class='label-value__value']")).text

    

    pdb.set_trace()




#     names_list.append(name)
#     titles_list.append(title)
#     specialities_list.append(speciality)
#     addresses_list.append(complete_addr)
#     counselors_list.append(rearranged_counselor)
#     accepting_new_patients_list.append(accepting_new_patients)




# data = {
#     'Name': names_list,
#     'Title': titles_list,
#     'Speciality': specialities_list,
#     'Address': addresses_list,
#     'Counselor': counselors_list,
#     'Accepting New Patients': accepting_new_patients_list,
# }



# df = pd.DataFrame(data)
# print(df)





