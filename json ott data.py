import json

file_new = "ottdata.json"

with open(file_new, "r") as panzer:
    data = json.load(panzer)

empty={}
for i in data["ott_data"]:
    if i["do"] == "null":
       mag_1=(f'{i["name"]} .{i["live"]} @gmail.com')
       empty[mag_1]={"name":i["name"],
                     "do":i["do"],"live":i["live"]}
        
    elif i["live"] =="null":
        mag_2=(f'{i["name"]}{i["do"]} @gmail.com')
        empty[mag_2]={"name":i["name"],
                     "do":i["do"],"live":i["live"]}

    else:
       mag_3=(f'{i["name"]} {i["do"]} {i["live"]} @gmail.com')
       empty[mag_3]={"name":i["name"],
                     "do":i["do"],"live":i["live"]}
new=json.dumps(empty)
print(new)
