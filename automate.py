from selenium import webdriver
from selenium.webdriver.common.keys import Keys #This is the class of different keys ex.RETURN
import time


#This is the driver object instancated form the chrome() class
driver = webdriver.Chrome()


#Get the link you wanted to search
driver.get("https://amazon.com")

#Wait till the page loads //clear this code and find a new function.
#This is errorsome

driver.implicitly_wait(5)

#This is a search object instanceated form the find_element class

search = driver.find_element("id","twotabsearchtextbox")

#sending the key arguments in the methods provided by the element class!!
search.send_keys("pokemon cards")
search.send_keys(Keys.RETURN)

source_code = driver.page_source

file = open("/home/vansha/Desktop/Project/automate/Automate/pokemon.html","w")
file.write(source_code)

time.sleep(10)

driver.quit