import requests
url = "https://script.googleusercontent.com/macros/echo?user_content_key=I7QkQbUMn2QIWYnyY3hAAVj1Tef2Vv8fYFjfNS7r2vD6ZyJmbKYJAoMMXseMKagsAszlAg0MVI5kLWVWi0XQeiJD_41cu4a9m5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnDtNDWjeuWDROys4STa1n3iy66YcPE2tCAtYljTjb5iT593JbaIWORpykOQk7fgST4Oqi87BQnusEPZvsV4FRx86EM9nFAad3dz9Jw9Md8uu&lib=M8MKZZyCrPXrHWAlUq0PPUY8mywudC-O8"
response = requests.get(url)
our_goods = response.json()
goods = our_goods.get("goods",[])
price_of_all_goods = []
price_gluten_free_list=[]
for good in goods:
    price = good.get("price", 0)
    price_of_all_goods.append(price)
    if good.get("gluten_containing",0) == False:
      price_gluten_free_list.append(price)

print(sum(price_of_all_goods))
print(sum(price_gluten_free_list))


