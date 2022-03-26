from entity_classes.deck import Deck


# this class allows us to easily store clash royale player details, and a players deck as a deck object
class Player:
    username: str
    player_tag: str
    clan_tag: str or None
    clan_name: str or None
    clan_badge_id: int or None
    player_deck: Deck
    original_player_dict: dict

    def __init__(self, player_dict: dict):
        self.username = player_dict["name"]
        self.player_tag = player_dict["tag"]
        try:
            self.clan_tag = player_dict["clan"]["tag"]
            self.clan_name = player_dict["clan"]["name"]
            self.clan_badge_id = player_dict["clan"]["badgeId"]
        # if we get a key error for clan info, that player doesn't belong to a clan
        except KeyError:
            self.clan_tag = None
            self.clan_name = None
            self.clan_badge_id = None
        self.player_deck = Deck(list_of_card_dicts=player_dict["cards"])
        self.original_player_dict = player_dict

    def __str__(self):
        player_dict = {"Player":
                       {"username": self.username,
                        "player_tag": self.player_tag,
                        "clan_tag": self.clan_tag,
                        "clan_name": self.clan_name,
                        "clan_badge_id": self.clan_badge_id,
                        "player_deck": self.player_deck
                        }
                       }
        # return player_dict.__str__()
        return self.original_player_dict.__str__()

    def __repr__(self):
        return self.__str__()




