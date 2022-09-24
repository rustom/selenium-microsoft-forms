import json
import names

file = open('./selenium-data.json')
data = json.load(file)
data['tests'][0]['commands'][4]['value'] = names.get_first_name() + '.' + names.get_last_name() + '@rustom.dev'
file 

with open("selenium-output.side", "w") as outfile:
    json.dump(data, outfile)