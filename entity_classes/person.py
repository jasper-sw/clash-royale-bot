from cr_client import CrClient
from send_text import SmsAlert


class Person:
    player_tag: str
    text_client: SmsAlert
    cell_number: int
    last_battle_info = None

    def __init__(self, player_tag: str, cell_number: int):
        self.player_tag = player_tag
        self.cell_number = cell_number
        self.text_client = SmsAlert(to=self.cell_number)
        self.text_client.config_from_file(config_path="twilio_config/twilio.txt")

    def __str__(self):
        person_dict = {"Person":
                       {"player_tag": self.player_tag,
                        "cell_number": self.cell_number,
                        }
                       }
        return person_dict.__str__()

    def __repr__(self):
        return self.__str__()

    def get_cell_number(self):
        return self.cell_number

    def get_player_tag(self):
        return self.player_tag

    def send_message(self, message):
        self.text_client.send_message(message=message)
