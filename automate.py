from selenium import webdriver
from selenium.webdriver.common.keys import Keys #This is the class of different keys ex.RETURN
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



#This is the driver object instancated form the chrome() class
driver = webdriver.Chrome()


#Get the link you wanted to search
driver.get("https://amazon.com")

print(driver.title)
#Wait till the page loads //clear this code and find a new function.
#This is errorsome



#This is a search object instanceated form the find_element class
    #This is created after the page have loaded the element you have specified

search = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.ID,"twotabsearchtextbox"))
)


#sending the key arguments in the methods provided by the element class!!
search.send_keys("pokemon cards")
search.send_keys(Keys.RETURN)



#tit_element = driver.find_element(By.CLASS_NAME,"a-size-base-plus a-color-base a-text-normal")

search_result = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="search"]/div[1]/div[1]'))
)


# this = driver.find_element(By.CSS_SELECTOR,'#search > div.s-desktop-width-max.s-desktop-content.s-wide-grid-style-t1.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(6) > div > div > div > div > div > div > div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small > div.a-section.a-spacing-none.a-spacing-top-small.s-price-instructions-style > div    ')

#You can also search with Xpath too with '//*[@id="search"]/div[1]/div[1]' as the Xpath

# single_result_elements = search_result.find_elements(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]')

single_result_elements = search_result.find_elements(By.CLASS_NAME,"s-widget-container")




for result in single_result_elements:
    print(result.text)

    
driver.quit
