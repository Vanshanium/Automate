import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import helper_functions
"""

"""
def result_discombobulator(url_string,search_string):

    driver = webdriver.Chrome() 
    #This opens the chrome webdriver if this function fails then input the address of the webdriver of the browser

    driver.get(url_string) 
    #This opens the chrome and searchs for the input url

    search_results = driver.find_elements(By.CLASS_NAME,"s-widget-container")
    #This is a html element searched from the class

    for result in search_results:

        if search_string in helper_functions.string_lizol(result.text):
            print(f"This is in the element:{result.text}")
            
        

"""
Parameters - It takes in a search_string(The thing you wanna search)
Return - It returns the json file with all the results along with prices and ratings!!!!
"""

def search_amazon(search_string):
    
    search_string = search_string.replace(' ','+')
   
    url = f"https://amazon.in/s?k={search_string}"

    result_discombobulator(url,helper_functions.string_lizol(search_string))



search_amazon("spider man into the spiderverse")


    