from entity_classes.person import Person
from entity_classes.battle import Battle
import time
from clash_bot import ClashBot
from cr_client import CrClient

cb = ClashBot()
cr = CrClient(api_token_file='token_config/api-tokens.txt')
jasper = Person(cell_number=8015108393, player_tag="#LCJ8RPLPR", name="Jasper")
jasper.last_battle_time = cr.get_last_battle_time(player_tag=jasper.player_tag)
john = Person(cell_number=8017122161, player_tag="#Y08P2PRLP", name="John")
john.last_battle_time = cr.get_last_battle_info(player_tag=john.player_tag)
hayden = Person(cell_number=3852144611, player_tag="#QJQU0J89C", name="Hayden")
hayden.last_battle_time = cr.get_last_battle_info(player_tag=hayden.player_tag)
justin = Person(cell_number=8019277910, player_tag="#QJVPGPLGG", name="Justin")
justin.last_battle_time = cr.get_last_battle_info(player_tag=justin.player_tag)


# people = [jasper, john, hayden, justin]
people = [jasper]


not_done = True
print("Starting ClashBot")
while not_done:
    time.sleep(1)

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


