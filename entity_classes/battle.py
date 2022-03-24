from entity_classes.player import Player


class Battle:
    battle_type: str
    battle_time: str
    is_ladder_tournament: bool
    arena_id: int
    arena_name: str
    game_mode_id: int
    game_mode_name: str
    deck_selection: str
    team: list
    team_battle_stats: list
    opponent: list
    opponent_battle_stats: list
    is_hosted_match: bool
    original_battle_dict: dict

    def __init__(self, battle_dict: dict):
        self.battle_type = battle_dict["type"]
        self.battle_time = battle_dict["battleTime"]
        self.is_ladder_tournament = battle_dict["isLadderTournament"]
        self.arena_id = battle_dict["arena"]["id"]
        self.arena_name = battle_dict["arena"]["name"]
        self.game_mode_id = battle_dict["gameMode"]["id"]
        self.game_mode_name = battle_dict["gameMode"]["name"]
        self.deck_selection = battle_dict["deckSelection"]
        self.team = []
        self.opponent = []
        self.team_battle_stats = []
        self.opponent_battle_stats = []

        for player_dict in battle_dict["team"]:
            player = Player(player_dict=player_dict)
            self.team_battle_stats.append(player_dict)
            self.team.append(player)

        for player_dict in battle_dict["opponent"]:
            player = Player(player_dict=player_dict)
            self.opponent_battle_stats.append(player_dict)
            self.opponent.append(player)

        self.is_hosted_match = battle_dict["isHostedMatch"]
        self.original_battle_dict = battle_dict

    def __str__(self):
        battle_dict = {"Battle":
                       {"battle_type": self.battle_type,
                        "battle_time": self.battle_time,
                        "is_ladder_tournament": self.is_ladder_tournament,
                        "arena_id": self.arena_id,
                        "arena_name": self.arena_name,
                        "game_mode_id": self.game_mode_id,
                        "game_mode_name": self.game_mode_name,
                        "deck_selection": self.deck_selection,
                        "team": self.team,
                        "team_battle_stats": self.team_battle_stats,
                        "opponent": self.opponent,
                        "opponent_battle_stats": self.opponent_battle_stats,
                        "is_hosted_match": self.is_hosted_match
                        }
                       }
        # return battle_dict.__str__()
        return self.original_battle_dict.__str__()

    def __repr__(self):
        return self.__str__()




