#Є два довільних числа які відповідають за мінімальну і максимальну ціну.
#Є Dict з назвами магазинів і цінами:
#{ "citos": 47.999, "BB_studio" 42.999, "mo-no": 49.999, "my-main-service": 37.245, "buy-now": 38.324, "x-store": 37.166, "the-partner": 38.988, "store-123": 37.720, "roze-tka": 38.003}.
#Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких потрапляють в діапазон
#між мінімальною і максимальною ціною.
#lower_limit = 35.9
#upper_limit = 37.339
#> match: "x-store", "main-service"

my_dict = { "citos": 47.999,
         "BB_studio": 42.999,
         "mo-no": 49.999,
         "my-main-service": 37.245,
         "buy-now": 38.324,
         "x-store": 37.166,
         "the-partner": 38.988,
         "store-123": 37.720,
         "roze-tka": 38.003
         }
lower_limit = 38.0
upper_limit = 40.0
list1 = []
for key, value in my_dict.items():
 if value > lower_limit and value < upper_limit:
         list1.append(f"{key}")
print(list1)






