#Є стрінг з певним текстом (можна скористатися input або константою).
# Напишіть код, я#кий визначить кількість слів в
# цьому тексті, які закінчуються на "о" (враховуються як великі так і маленькі)
import re

# виводити число слів з буквою "o"
text = input("Enter text: ").lower()
split = text.split(" ")
count = []
for elem in split:
    if elem.find("o") > -1:
        count.append(elem)
print(len(count))

#виводить слова які містять букву "o"
text = input("Enter text: ").lower()
split = text.split(" ")
for elem in split:
    if elem.find("0") > 1:
        print(elem)

text = input("Enter text: ").lower()
reg = re.compile('[^a-zA-Z 0-9]')
new_text = (reg.sub('', text))
split = new_text.split(" ")
print(split)
count = []
for elem in split:
    if elem[-1] == "o":
     count.append(elem)
print(len(count))










