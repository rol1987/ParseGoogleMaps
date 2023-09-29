
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import csv
import time
from selenium.webdriver.chrome.service import Service
import bs4
import lxml

search = "dentista Palazzolo sull Oglio	"
pages = 2
header = ["data_cid", "title", "address", "website", "phone", "rating","reviews","image","category","timing","description","profiles"]
data = []
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.3.904 Yowser/2.5 Safari/537.36")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
full_path_chromedriver = r'C:\Users\Olga\Desktop\ParseGoogleMaps\chromedriver.exe'
s = Service(full_path_chromedriver)
driver = webdriver.Chrome(service = s, options=options)
driver.get('https://www.google.com')

# driver.implicitly_wait(2)
driver.find_element(By.NAME,"q").send_keys(search + Keys.ENTER)
more = driver.find_element(By.TAG_NAME,"g-more-link")
more_btn = more.find_element(By.TAG_NAME,"a")
more_btn.click()
time.sleep(3)

elements = driver.find_elements(By.TAG_NAME, 'div')
i = 0
for element in elements:
    try:
        attribute = element.get_attribute('data-record-click-time')
        if attribute != None: i += 1
    except: print("Не получилось получить аттрибут")

print(i)
l = 0
k = 1
ind = 1
while ind == 1:
    
    print(l, i)
    try:
        next = driver.find_elements(By.TAG_NAME,"span")
    except:
        next = driver.find_elements(By.TAG_NAME,"span")

    for count in next:
        
        if count.text == "Далее" and k != 0:
            count.click()
            time.sleep(10)
            elements = driver.find_elements(By.TAG_NAME, 'div')
            # print(l)
            k = 0
            for element in elements:
                try:
                    attribute = element.get_attribute('data-profile-url-path')
                    if attribute != None:
                        k += 1
                        i += 1
                except:
                    print('ошибка')
            if k == 0:
                ind = 0
                break
            else:
                ind = 1
            continue
    l  += 1  

print(i)
        



time.sleep(5)
# next = driver.find_element(By.TAG_NAME,"g-more-link")
# more_btn = more.find_element(By.TAG_NAME,"a")
driver.quit()
driver.close()

