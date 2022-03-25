from entity_classes.card import Card


# this class allows us to easily store the deck for a player as a collection of card objects
class Deck:
    cards_list = []
    original_list_of_card_dicts: list

    # takes an array of dicts ([{}, {}, ..., {}]) where each dict is a set of card details formatted the
    #   same was as the supercell api returns them by default
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
