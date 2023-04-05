
from pprint import pprint
#вивести в консоль середній вік чоловіків з Brown волоссям, а також сформувати список людей,
# що проживають в місті Louisville. Реалізація якщо потрібно окремо порахувати середній вік людей з коричньовим волоссям
# та окремо зробити вибірку людей які живуть  в місті Louisville
import requests
import numpy as np
url = "https://dummyjson.com/users?limit=100"
response = requests.get(url)
our_users = response.json()
users_hair = response.json()
users = our_users.get("users",[])
age_list = []
users_from_one_city = []
for user in users:
 hair = user.get("hair")
 age = user.get("age")
 if hair.get("color") == "Brown":
  age_list.append(age)
print(int(np.mean(age_list)))
for user in users:
 address = user.get("address")
 if address.get("city") == "Louisville":
  users_from_one_city.append(user)
print(users_from_one_city)






