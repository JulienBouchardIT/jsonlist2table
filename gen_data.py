import random
import json

# Generate a random list of objects
def generate_random_objects(num_objects):
    objects = []
    for _ in range(num_objects):
        obj = {
            "id": random.randint(1000, 1999),
            "firstname": random.choice(["John", "Alice", "Bob", "Jane"]),
            "lastname": random.choice(["Doe", "Smith", "Johnson", "Williams"]),
            "grocery": ["potato","tomato","avocado"]
        }
        objects.append(obj)
    return objects

# Number of objects to generate
num_objects = 50

# Generate random objects
objects_list = generate_random_objects(num_objects)

# Convert the list of objects to JSON
json_data = json.dumps(objects_list, indent=4)

f = open("page/data.json", "w")
f.write(json_data)
f.close()
