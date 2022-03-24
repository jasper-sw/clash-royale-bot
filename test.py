from entity_classes.person import Person
from cr_client import CrClient
from entity_classes.battle import Battle

jasper = Person(cell_number=8015108393, player_tag="#LCJ8RPLPR")
cr = CrClient(api_token_file='token_config/api-tokens.txt', player_tag=jasper.player_tag)

log = cr.get_last_battle_info()
print("LOG: ")
print(log)
print("")
battle = Battle(battle_dict=log)
print(battle)

