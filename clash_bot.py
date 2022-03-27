import random


# this class contains variables and logic for texting annoying messages to friends after they play clash games
class ClashBot:
    # messages to send players based on whether they lose or win, and how many crowns they get
    one_crown_loss_messages = ["[ClashBot] 1 crown... L bro",
                               "[ClashBot] 1 crown bro... gotta do better",
                               "[ClashBot] Hey at least you got 1 tower!",
                               "[ClashBot] Could have been worse, you could have got 0 crowns",
                               "[ClashBot] Matchmaking is rigged bro!",
                               "[ClashBot] L+RATIO RIP BOZO",
                               "[ClashBot] LMAO"]

    two_crown_loss_messages = ["[ClashBot] 2 crown... L bro",
                               "[ClashBot] 2 crowns... close but not quite",
                               "[ClashBot] You almost had that one, only needed 1 more",
                               "[ClashBot] Really thought you had that one",
                               "[ClashBot] Robbed tbh",
                               "[ClashBot] Matchmaking is rigged bro!",
                               "[ClashBot] LMAO"]

    zero_crown_loss_messages = ["[ClashBot] 0 crown... L bro",
                                "[ClashBot] No crowns no skill bro",
                                "[ClashBot] R.I.P. 0 crowns bro",
                                "[ClashBot] Maybe you'll do better next time",
                                "[ClashBot] Not everyone is cut out for this, its alright",
                                "[ClashBot] Maybe you should think about a new deck",
                                "[ClashBot] Ass?",
                                "[ClashBot] Matchmaking is rigged bro!",
                                "[ClashBot] L+RATIO RIP BOZO",
                                "[ClashBot] LMAO"]

    one_crown_win_messages = ["[ClashBot] 1 crown W bro!",
                              "[ClashBot] That last one was a win... but barely",
                              "[ClashBot] Hard fought win!",
                              "[ClashBot] 1 crown to rule them all"]

    two_crown_win_messages = ["[ClashBot] 2 crown W bro!",
                              "[ClashBot] Solid win bro",
                              "[ClashBot] Can't hate on a 2 crown",
                              "[ClashBot] Respectable. Have a nice day",
                              "[ClashBot] 2 crown king right here",
                              "[ClashBot] No BOZOs here"]

    three_crown_win_messages = ["[ClashBot] 3 crown W bro!",
                                "[ClashBot] Lets gooo that's a W",
                                "[ClashBot] Brutally destructive 3 crown",
                                "[ClashBot] That guy was ass",
                                "[ClashBot] Another day another dub",
                                "[ClashBot] GOAT?",
                                "[ClashBot] He didn't even stand a chance",
                                "[ClashBot] Hog Riiiiidaaaaa"]

    def __init__(self):
        pass

    # randomly return a crown loss message based on crowns won
    def crown_loss_message(self, crown_count: int):
        if crown_count == 0:
            num = random.randint(0, (len(self.zero_crown_loss_messages) - 1))
            return self.zero_crown_loss_messages[num]
        elif crown_count == 1:
            num = random.randint(0, (len(self.one_crown_loss_messages) - 1))
            return self.one_crown_loss_messages[num]
        elif crown_count == 2:
            num = random.randint(0, (len(self.two_crown_loss_messages) - 1))
            return self.two_crown_loss_messages[num]

    # randomly return a crown win message based on crowns won
    def crown_win_message(self, crown_count: int):
        if crown_count == 1:
            num = random.randint(0, (len(self.one_crown_win_messages) - 1))
            return self.one_crown_win_messages[num]
        elif crown_count == 2:
            num = random.randint(0, (len(self.two_crown_win_messages) - 1))
            return self.two_crown_win_messages[num]
        elif crown_count == 3:
            num = random.randint(0, (len(self.three_crown_win_messages) - 1))
            return self.three_crown_win_messages[num]

    def crown_message(self, crown_count: int, win: bool):
        if win is True:
            return self.crown_win_message(crown_count=crown_count)
        elif win is False:
            return self.crown_loss_message(crown_count=crown_count)


