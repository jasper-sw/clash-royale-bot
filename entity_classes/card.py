
class Card:
    name: str
    card_id: int
    level: int
    star_level: int or None
    max_level: int
    icon_urls: dict
    original_card_dict: dict

    def __init__(self, card_dict):
        self.name = card_dict["name"]
        self.card_id = card_dict["id"]
        self.level = card_dict["level"]
        try:
            self.star_level = card_dict["starLevel"]
        except KeyError:
            self.star_level = None
        self.max_level = card_dict["maxLevel"]
        self.icon_urls = card_dict["iconUrls"]
        self.original_card_dict = card_dict

    def __str__(self):
        card_dict = {"Card":
                       {"name": self.name,
                        "card_id": self.card_id,
                        "level": self.level,
                        "star_level": self.star_level,
                        "max_level": self.max_level,
                        "icon_urls": self.icon_urls
                        }
                       }
        # return card_dict.__str__()
        return self.original_card_dict.__str__()

    def __repr__(self):
        return self.__str__()



