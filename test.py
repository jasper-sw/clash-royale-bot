import datetime

from entity_classes.person import Person
from cr_client import CrClient
from entity_classes.battle import Battle

# jasper = Person(cell_number=8015108393, player_tag="#LCJ8RPLPR")
# cr = CrClient(api_token_file='token_config/api-tokens.txt')
#
# log = cr.get_last_battle_info(player_tag=jasper.player_tag)
# print("LOG: ")
# print(log)
# print("")
# battle = Battle(battle_dict=log)
#
# print(battle.get_battle_time_12_hour_local())

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
