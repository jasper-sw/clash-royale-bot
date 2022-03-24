import requests.utils
from requests.structures import CaseInsensitiveDict
from dateutil import parser
import datetime
from datetime import datetime, timezone
import os


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

    def __init__(self, api_token_file: str = None, api_token: str = None, player_tag: str = None):
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

        self.player_tag = self.ensure_player_tag(player_tag)

    # setup Bearer token auth headers
    def set_request_headers(self):
        self.headers = CaseInsensitiveDict()
        self.headers["Accept"] = "application/json"
        self.headers["Authorization"] = ("Bearer {}".format(self.api_token))

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

    def url_encode_string(self, string: str):
        return requests.utils.quote(string)

    def ensure_player_tag(self, player_tag: str):
        if player_tag is None and self.player_tag is None:
            raise SystemExit("ERROR: must supply player_tag for lookup!")
        elif player_tag is None:
            return self.player_tag
        else:
            return player_tag

    def get_last_battle_info(self, player_tag: str = None):
        player_tag = self.ensure_player_tag(player_tag=player_tag)

        response = self.get_player_battle_log(player_tag=player_tag)
        return response[0]

    def get_time_since_last_battle(self, player_tag: str = None):
        player_tag = self.ensure_player_tag(player_tag=player_tag)

        response = self.get_player_battle_log(player_tag=player_tag)
        last_battle_time = parser.parse((response[0]["battleTime"]))
        current_time = datetime.now(timezone.utc)
        elapsed_time = current_time - last_battle_time
        return elapsed_time

    def get_player_battle_log(self, player_tag: str = None):
        player_tag = self.ensure_player_tag(player_tag=player_tag)

        player_tag = self.url_encode_string(player_tag)
        url = self.base_url + self.players_string + player_tag + self.battle_log_string
        response = requests.get(url=url, headers=self.headers)
        return response.json()

    def get_player_info(self, player_tag: str = None):
        player_tag = self.ensure_player_tag(player_tag=player_tag)

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
        player_tag = self.ensure_player_tag(player_tag=player_tag)

        player_tag = self.url_encode_string(player_tag)
        url = self.base_url + self.players_string + player_tag + self.upcoming_chests_string
        response = requests.get(url=url, headers=self.headers)
        return response.json()


