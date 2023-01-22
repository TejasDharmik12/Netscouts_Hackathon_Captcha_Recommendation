from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
options = Options()
userAget = "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
# options.add_argument('user-agent', userAget)

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(executable_path="C:\\SeleniumDriver\\chromedriver.exe", chrome_options=options)
time.sleep(3)  


driver.get("https://faijanmomin.vittnt.in/")  

# WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.div")))
nifty_box = driver.find_element(By.XPATH, "/html/body/header/div/div[3]/div[1]/ul/li[4]/a")  
time.sleep(2)  
nifty_box.click()
# driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)  
time.sleep(3)  
# driver.close()  
print("sample test case successfully completed")  