import json

new_dict={'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
with open("./config/record.json","w") as f:
   json.dump(new_dict,f)

with open("./config/record.json",'r') as load_f:
  load_dict = json.load(load_f)
  print(load_dict)