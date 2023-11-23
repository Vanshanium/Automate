from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.amazon.in/s?k=pokemon")

results = driver.find_elements(By.CLASS_NAME,"s-widget-container")


print(results[3].text)
# i = 0
# for i in range(1,70):
#     i += 1
#     print(result.text)

# print(i)
