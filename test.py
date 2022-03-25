import datetime

from entity_classes.person import Person
from cr_client import CrClient
from entity_classes.battle import Battle
import json
people = {}
with open('people.txt') as file:
    lines = file.readlines()

data = json.loads(str(lines[0]))
people_dict = dict(data)
# print(people_dict)

people_list = []

for person in people_dict.keys():
    curr_person = Person(cell_number=people_dict[person]["cell_number"], player_tag=people_dict[person]["tag"])
    people_list.append(curr_person)
print(people_list)
