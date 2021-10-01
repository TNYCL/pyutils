import random
import json
import os

def generate():
    names = os.getcwd() + '/names.json'
    with open(names) as file:
        data = json.load(file)
        first_names = data['first_names']
        last_names = data['last_names']
    return '{} {}'.format(random.choice(first_names), random.choice(last_names))

print(generate())