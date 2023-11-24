# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome()

# driver.get("https://www.amazon.in/s?k=spider+man+into+the+spider+verse")

# results = driver.find_elements(By.CLASS_NAME,"s-widget-container")

# # price = results[4].find_element(By.CLASS_NAME,'a-price-whole')

# title = results[4].find_element(By.CLASS_NAME,'a-size-base-plus')

# print(title.text)

# index = 0

# for result in results:

#     if (index == 0 and index == 1):
#         print("weee")
#         index += 1
#     if (index == 2 and index == 3):
#         index += 1
    
#     else:

#         print(result.text)

#         title = result.find_element(By.CLASS_NAME,'a-size-base-plus')
#         print(title.text)



dict = {}

for i in range(1,10):
    dict['first_element'][i] = i
    dict['second_element'][i] = i+1

print(dict)