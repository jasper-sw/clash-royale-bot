from entity_classes.person import Person
from entity_classes.battle import Battle
import time
from clash_bot import ClashBot
from cr_client import CrClient
import json

cb = ClashBot()
cr = CrClient(api_token_file='token_config/api-tokens.txt')

# open people config file and get player tags, numbers, names
with open('people.txt') as file:
    lines = file.readlines()
data = json.loads(str(lines[0]))
people_dict = dict(data)

# create list of people
people = []
for person in people_dict.keys():
    curr_person = Person(cell_number=people_dict[person]["cell_number"], player_tag=people_dict[person]["tag"], name=person)
    curr_person.last_battle_time = cr.get_last_battle_time(player_tag=curr_person.player_tag)
    people.append(curr_person)

not_done = True
print("Starting ClashBot")
while not_done:
    time.sleep(3)

    for homie in people:
        time.sleep(1)
        recent_battle = Battle(battle_dict=cr.get_last_battle_info(player_tag=homie.player_tag))
        recent_battle_time = recent_battle.get_battle_time()
        last_battle_time = homie.last_battle_time
        elapsed = recent_battle_time - last_battle_time
        # print("recent battle time: {}, last battle time: {}".format(recent_battle_time, last_battle_time))
        # print("{} elapsed time: {}".format(homie.name, elapsed))
        # print("total seconds: {}".format(elapsed.total_seconds()))

        if (elapsed.total_seconds() != 0) and (homie.last_battle_time != recent_battle_time):
            crowns = recent_battle.get_player_team_crowns()
            win_status = recent_battle.get_team_win_status()

            print("\n{} recently entered a game! Time since last battle: {}".format(homie.name, elapsed))
            message = cb.crown_message(crown_count=crowns, win=win_status)
            print("win status: {}, crown count: {}".format(win_status, crowns))
            homie.send_message(message=message)
            print("Send message: [\'{}\'] to {} at number: {}\n".format(message, homie.name, homie.cell_number))
            homie.last_battle_time = recent_battle_time


