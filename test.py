import requests
import csv

BASE = "http://127.0.0.1:5000/"

# 0 = Name
# 1 = Alignment
# 2 = Image

with open("allegiance.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 1
    for row in reader:
        data = {
            'name': row[0],
            'alignment': row[1],
            'image': row[2]
        }

        response = requests.put(BASE + "allegiance/" + str(i), data=data)
        print(response.json())

        i = i + 1