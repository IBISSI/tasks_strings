import json
from pprint import pprint
from pprint import pprint
with open('template.json') as f:
    file_content = f.read()
    template = json.loads(file_content)

print (template)
model = template
print("------------------------------------------------------------------------------")
for switch in model.keys():
    if model[switch]['10/100Mbps'] == "5x" and \
            model[switch]['Mac adress entries'] == "1k":
        pprint(model[switch])