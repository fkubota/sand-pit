import yaml

# load yaml
with open('config.yaml', 'r') as yml:
    config = yaml.safe_load(yml)

print(config)


# save yaml
obj = {'x': 'XXX', 'y': 100, 'z': [200, 300, 400]}
with open('output.yaml', 'w') as file:
    yaml.dump(obj, file)
