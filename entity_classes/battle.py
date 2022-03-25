from entity_classes.player import Player
import datetime
from dateutil import tz


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

    def get_player_crowns(self, player_tag: str):
        all_battle_stats = []
        all_battle_stats.extend(self.team_battle_stats)
        all_battle_stats.extend(self.opponent_battle_stats)
        for entry in all_battle_stats:
            if entry["tag"] == player_tag:
                return entry["crowns"]

        return None

    def get_player_team_crowns(self):
        total_crowns = 0
        for entry in self.team_battle_stats:
            total_crowns += entry["crowns"]
        return total_crowns

    def get_opponent_team_crowns(self):
        total_crowns = 0
        for entry in self.opponent_battle_stats:
            total_crowns += entry["crowns"]
        return total_crowns

    def get_battle_time(self):
        return datetime.datetime.strptime(self.battle_time, "%Y%m%dT%H%M%S.%fZ")

    def get_battle_time_12_hour_local(self):
        from_zone = tz.gettz('UTC')
        to_zone = tz.tzlocal()
        battle_time = datetime.datetime.strptime(self.battle_time, "%Y%m%dT%H%M%S.%fZ")
        battle_time = battle_time.replace(tzinfo=from_zone)
        battle_time = battle_time.astimezone(to_zone)
        battle_time = battle_time.strftime("%I:%M %p")
        return battle_time

    def get_team_win_status(self):
        player_team_crowns = self.get_player_team_crowns()
        opponent_team_crowns = self.get_opponent_team_crowns()

        if player_team_crowns > opponent_team_crowns:
            return True
        else:
            return False

