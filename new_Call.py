import csv
a="asad"
b="ali"
c="data"

with open('students.csv', 'a', newline='') as file:
     writer = csv.writer(file)
     
     writer.writerow([a,b,c])
     writer.writerow([1, "Ash Ketchum", "English"])
     writer.writerow([2, "Gary Oak", "Mathematics"])
     writer.writerow([3, "Brock Lesner", "Physics"])
