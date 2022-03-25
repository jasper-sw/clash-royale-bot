import requests.utils
from requests.structures import CaseInsensitiveDict
from entity_classes.battle import Battle
from dateutil import parser
import datetime
from datetime import datetime, timezone
import os


# this class allows us to easily interface with the official supercell clash royale api
class CrClient:
    # the working/current api token
    api_token: str
    # the list of api tokens and their names from the config file
    api_token_dict: dict
    player_tag: str
    # our request headers
    headers: CaseInsensitiveDict
    base_url = "https://api.clashroyale.com/v1"
    players_string = "/players/"
    battle_log_string = "/battlelog"
    upcoming_chests_string = "/upcomingchests"
    # characters to remove from api tokens
    bad_token_chars = ['\n', '\r']

    def __init__(self, api_token_file: str = None, api_token: str = None):
        if (api_token_file is None) and (api_token is None):
            raise SystemExit("CrClient: ERROR: You must supply either an api_token_file or an api_token! "
                             "Both were None")
        elif (api_token_file is not None) and (api_token is None):
            self.api_token_dict = self.get_tokens_from_config(token_config_path=api_token_file)
            self.find_working_token()
        elif (api_token_file is None) and (api_token is not None):
            self.api_token = api_token

        # ensure api token is cleaned up
        for char in self.bad_token_chars:
            self.api_token = self.api_token.replace(char, '')

    # setup Bearer token auth headers
    def set_request_headers(self):
        self.headers = CaseInsensitiveDict()
        self.headers["Accept"] = "application/json"
        self.headers["Authorization"] = ("Bearer {}".format(self.api_token))

    # run through the list of tokens in the token config file and find one that works. This is potentially
    #   useful because supercell forces you to create a non-mutable list of ip addresses for each api token you create
    def find_working_token(self):
        for key in self.api_token_dict.keys():
            curr_token = self.api_token_dict[key]
            self.api_token = curr_token
            self.set_request_headers()
            response = self.get_cards()
            if not ((dict(response).keys().__contains__('reason')) and (response['reason'] == "accessDenied.invalidIp")):
                print("Found working api_token! Key: {}, Value: {}\n".format(key, self.api_token_dict[key]))
                return
        raise SystemExit("CrClient: ERROR: Unable to find a working api token in the config file!")

    # get all api tokens from the config file at token_config/api-tokens.txt
    def get_tokens_from_config(self, token_config_path: str):
        if not os.path.exists(token_config_path):
            raise SystemExit("CrClient: ERROR: Token config filepath does not exist!")

        all_tokens = {}
        with open(token_config_path, 'r') as file:
            for line in file:
                line = line.rstrip()
                line_split = line.split('=')
                for x in line_split:
                    if 3 < len(x) < 400:
                        x_index = list(line_split).index(x)
                        all_tokens[x] = line_split[x_index + 1]

        print("\nCrClient: Found {} tokens in config file: \'{}\'. Listed: ".format(len(all_tokens.keys()), token_config_path))
        for x in all_tokens.keys():
            print("{}: {}".format(x, all_tokens[x]))

        return all_tokens

    # url encode player tags
    def url_encode_string(self, string: str):
        return requests.utils.quote(str(string))

    # this function returns the details for the last battle in a players battle log given a player tag
    def get_last_battle_info(self, player_tag: str = None):
        response = self.get_player_battle_log(player_tag=player_tag)
        try:
            return response[0]
        except KeyError:
            print("CrClient: ERROR: Couldn't get last battle for player_tag: {}".format(player_tag))
            return None

    def get_time_since_last_battle(self, player_tag: str = None):
        response = self.get_player_battle_log(player_tag=player_tag)
        last_battle_time = parser.parse((response[0]["battleTime"]))
        current_time = datetime.now(timezone.utc)
        elapsed_time = current_time - last_battle_time
        return elapsed_time

    # return the time that the last battle took place for a player given their player tag
    def get_last_battle_time(self, player_tag: str = None):
        last_battle = Battle(self.get_last_battle_info(player_tag=player_tag))
        return last_battle.get_battle_time()

    def get_player_battle_log(self, player_tag: str = None):
        player_tag = self.url_encode_string(player_tag)
        url = self.base_url + self.players_string + player_tag + self.battle_log_string
        response = requests.get(url=url, headers=self.headers)
        return response.json()

    def get_player_info(self, player_tag: str = None):
        player_tag = self.url_encode_string(player_tag)
        url = self.base_url + self.players_string + player_tag
        response = requests.get(url=url, headers=self.headers)
        return response.json()

    # get a list of all available cards in the game
    def get_cards(self):
        url = self.base_url + "/cards"
        response = requests.get(url=url, headers=self.headers)
        return response.json()

    def get_player_upcoming_chests(self, player_tag: str = None):

        player_tag = self.url_encode_string(player_tag)
        url = self.base_url + self.players_string + player_tag + self.upcoming_chests_string
        response = requests.get(url=url, headers=self.headers)
        return response.json()


