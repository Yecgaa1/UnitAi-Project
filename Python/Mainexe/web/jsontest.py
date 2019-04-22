import json

new_dict={'123': 123}
with open("./config/record.json","w") as f:
   json.dump(new_dict,f)

with open("./config/record.json",'r') as load_f:
  load_dict = json.load(load_f)
  print(load_dict)