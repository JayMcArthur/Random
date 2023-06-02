import os, json, uuid

rank_points = {
    'Pro': 1,
    'Senior': 2,
    'Master': 3,
    'Premier': 4,
    'Elite': 5,
    'Diamond': 6
}

# 3 or more new customers = 1
# 3 or more new wellness = 1
# 150+ wellness = 1


filename = 'distributors.json'
with open(filename, 'r') as f:
    data = json.load(f)
    data['id'] = 134

tempfile = os.path.join(os.path.dirname(filename), str(uuid.uuid4()))
with open(tempfile, 'w') as f:
    json.dump(data, f, indent=4)

os.replace(tempfile, filename)