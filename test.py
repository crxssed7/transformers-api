import requests
import csv

BASE = "http://127.0.0.1:5000/"

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

#with open("tf_extra_details.csv", newline='') as csvfile:
#    reader = csv.reader(csvfile, delimiter='|', quotechar='"')
#    for row in reader:
#        data = {
#            'description': row[2]
#        }
#
#        response = requests.patch(BASE + "transformers/" + str(row[0]), data=data)
#        print(response.json())

response = requests.delete(BASE + "transformers/131")
print(response)