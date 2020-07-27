import json

l = '1,2,3,4,5,6,7,8,9'

with open('json_res.json','w') as handle:
    json.dump(l,handle, indent=4)

