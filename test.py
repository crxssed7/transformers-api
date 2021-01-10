import requests
import csv

BASE = "http://192.168.1.15:5000/"

# 0 = Name
# 1 = Alignment
# 2 = Image

#with open("allegiance.csv", newline='') as csvfile:
#    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#    i = 1
#    for row in reader:
#        data = {
#            'name': row[0],
#            'alignment': row[1],
#            'image': row[2]
#        }
#
#        response = requests.put(BASE + "allegiance/" + str(i), data=data)
#        print(response.json())
#
#        i = i + 1

#with open("subgroup.csv", newline='') as csvfile:
#    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#    i = 1
#    for row in reader:
#        data = {
#            'name': row[0],
#            'alignment': row[1],
#            'image': row[2]
#        }
#
#        response = requests.put(BASE + "subgroup/" + str(i), data=data)
#        print(response.json())
#
#        i = i + 1

#with open("transformers.csv", newline='') as csvfile:
#    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#    i = 1
#    for row in reader:
#        data = {
#            'name': row[0],
#            'allegiance': row[1],
#            'subgroup': row[2],
#            'role': row[3],
#            'image': row[4]
#        }
#
#        response = requests.put(BASE + "transformers/" + str(i), data=data)
#        print(response.json())
#
#        i = i + 1

response = requests.get(BASE + "transformers/filter=allegiance_name&query=autobot&page=1")
print(response.json())