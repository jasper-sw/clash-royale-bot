import datetime

from entity_classes.person import Person
from cr_client import CrClient
from entity_classes.battle import Battle

jasper = Person(cell_number=8015108393, player_tag="#LCJ8RPLPR")
cr = CrClient(api_token_file='token_config/api-tokens.txt')

log = cr.get_last_battle_info(player_tag=jasper.player_tag)
print("LOG: ")
print(log)
print("")
battle = Battle(battle_dict=log)

print(battle.get_battle_time_12_hour_local())

