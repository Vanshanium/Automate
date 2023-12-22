import requests

"""
Parameters - It takes in a search_string(The thing you wanna search)
Return - It returns the json file with all the results along with prices and links!!!!
"""

def search_flipkart(search_string):
    
    search_string = search_string.replace(' ','+')

    url = f"https://flipkart/search?q={search_string}"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

    r = requests.get(url,headers=headers)

    print(r.status_code)


search_flipkart("pokemon cards")