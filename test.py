import json
"""""
data='{"name":"ali","Age":"15"}'
parsed= json.loads(data)
print(parsed["name"])
"""

data2 = {
    "player": "dembele",
    "position": "rw",
    "cars":["mustang","ford"],
    "boots":("nike","adidas")
}
jscomp=json.dumps(data2, indent=4, sort_keys=True)
print(jscomp) 
