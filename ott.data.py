import json

file_new = "ottdata.json"

with open(file_new, "r") as panzer:
    data = json.load(panzer)

for i in data["ott_data"]:
    if i["do"] == "null":
       print(f'{i["name"]} {i["do"]}.{i["live"]} @gmail.com')
        
    elif i["live"] =="null":
        print(f'{i["name"]}{i["do"]} @gmail.com')

    else:
       print(f'{i["name"]} {i["live"]} @gmail.com')