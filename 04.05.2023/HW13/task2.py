#Використайте прикріплений файл json та прочитайте його за допомогою модулю json.



import json

with open(r"C:\Users\Jack\Downloads\sample2.json") as f:
  data = json.load(f)
  print(data)