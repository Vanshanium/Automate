from amazon_scrap import search_amazon

json = search_amazon("thomas calculus")

print(json['product_list'])