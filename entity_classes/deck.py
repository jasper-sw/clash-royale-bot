from entity_classes.card import Card


class Deck:
    cards_list = []
    original_list_of_card_dicts: list

    def __init__(self, list_of_card_dicts: list):
        self.original_list_of_card_dicts = list_of_card_dicts

        for card_dict in list_of_card_dicts:
            curr_card = Card(card_dict)
            self.cards_list.append(curr_card)

    def __str__(self):
        deck_dict = {"Deck":
                         {"cards": self.cards_list}
                     }
        # return deck_dict.__str__()
        return self.original_list_of_card_dicts.__str__()

    def __repr__(self):
        return self.__str__()
