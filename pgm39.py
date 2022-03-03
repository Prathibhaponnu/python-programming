import csv
with open('people.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print('Name','Age')
 for row in data:
   print(row['Name'], row['Age'])
