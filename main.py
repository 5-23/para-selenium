from selenium import webdriver
from selenium.webdriver.common.by import By
import random, time

query = "sus"

driver = webdriver.Chrome()
driver.get(f"https://crates.io/search?q={query}")

time.sleep(1.5)
for i in driver.find_element(By.XPATH, "/html/body/main/div/div[3]/ol").find_elements(By.TAG_NAME, "li"):
    # a = i.find_element(By.CSS_SELECTOR, "li > div > div > div > a")
    try:

        name = i.find_element(By.TAG_NAME, "div").find_elements(By.TAG_NAME, "div")[0].find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "a").text
        all_time = i.find_element(By.TAG_NAME, "div").find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "div")[0].find_element(By.TAG_NAME, "span").text
        print(name)
        print()
    except: ...