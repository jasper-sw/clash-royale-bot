import random


class ClashBot:
    one_crown_loss_messages = ["[ClashBot] 1 crown... L bro",
                               "[ClashBot] 1 crown bro... gotta do better"]

    two_crown_loss_messages = ["[ClashBot] 2 crown... L bro",
                               "[ClashBot] 2 crowns... close but not quite"]

    zero_crown_loss_messages = ["[ClashBot] 0 crown... L bro",
                                "[ClashBot] No crowns no skill bro",
                                "[ClashBot] R.I.P. 0 crowns bro"]

    one_crown_win_messages = ["[ClashBot] 1 crown W bro!",
                              "[ClashBot] A win... but barely"]

    two_crown_win_messages = ["[ClashBot] 2 crown W bro!",
                              "[ClashBot] Solid win bro"]

    three_crown_win_messages = ["[ClashBot] 3 crown W bro!",
                                "[ClashBot] Lets gooo that's a W",
                                "[ClashBot] Do or do not, there is no try"]

    def __init__(self):
        pass

    def parse_battle_info(self, battle_info):
        player_crowns_won = battle_info["team"][0]["crowns"]
        opponent_crowns_won = battle_info["opponent"][0]["crowns"]
        battle_time = battle_info["battleTime"]
        battle_type = battle_info["gameMode"]["name"]

    def crown_loss_message(self, crown_count: int):
        if crown_count == 0:
            num = random.randint(0, (len(self.zero_crown_loss_messages) - 1))
            return self.zero_crown_loss_messages[num]
        elif crown_count == 1:
            num = random.randint(0, (len(self.one_crown_loss_messages) - 1))
            return self.zero_crown_loss_messages[num]
        elif crown_count == 2:
            num = random.randint(0, (len(self.two_crown_loss_messages) - 1))
            return self.zero_crown_loss_messages[num]

    def crown_win_message(self, crown_count: int):
        if crown_count == 1:
            num = random.randint(0, (len(self.one_crown_win_messages) - 1))
            return self.zero_crown_loss_messages[num]
        elif crown_count == 2:
            num = random.randint(0, (len(self.two_crown_win_messages) - 1))
            return self.zero_crown_loss_messages[num]
        elif crown_count == 3:
            num = random.randint(0, (len(self.three_crown_win_messages) - 1))
            return self.zero_crown_loss_messages[num]

    def crown_message(self, crown_count: int, win: bool):
        if win is True:
            return self.crown_win_message(crown_count=crown_count)
        elif win is False:
            return self.crown_loss_message(crown_count=crown_count)


