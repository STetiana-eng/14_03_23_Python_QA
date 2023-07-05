#Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.




import csv


with open(r"C:\Users\Jack\Downloads\SampleCSVFile_11kb.csv") as csvfile:
  csvfile_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in csvfile_reader:
    print(row)




