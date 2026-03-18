import json

data = {"name": "Alice", "role": "Dev", "active": True}

# 1
json_string = json.dumps(data, indent=4)

# 2
with open("user.json", "w") as f:
    json.dump(data, f)

# 3
parsed_dict = json.loads(json_string)

# 4
with open("user.json", "r") as f:
    loaded_data = json.load(f)

# 5
sorted_json = json.dumps(data, sort_keys=True)