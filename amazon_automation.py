from selenium import webdriver
from selenium.webdriver.common.keys import Keys #This is the class of different keys ex.RETURN
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#This is the driver object instancated form the chrome() class
driver = webdriver.Chrome()


#Get the link you wanted to search
driver.get("https://amazon.com")

print(driver.title)

#This is a element of the webpage and the code actually waits for the element to load 
#hence it a fail safe!
search = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.ID,"twotabsearchtextbox"))
)


#sending the key arguments in the methods provided by the element class!!
search.send_keys("pokemon cards")
search.send_keys(Keys.RETURN)

#Now on the search screan you will wait for all the elements to load on the page
search_result = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="search"]/div[1]/div[1]'))
)

#This is the Collection of all the result elements presend on the screan
single_result_elements = search_result.find_elements(By.CLASS_NAME,"s-widget-container")

#We are looping through all the single elements to show what result actually is 

# for result in single_result_elements:
#     print(result.text)

driver.find_element(By.ID,"nav-cart").send_keys(Keys.RETURN)


#refine the print string to just give the results and price!!!
    
driver.quit
