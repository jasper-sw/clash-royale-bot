from send_text import SmsAlert
import datetime


# this class allows us to store details for a person like name, player_tag, and phone number which we can use to
#   text them annoying and degrading messages in the real world when they lose games in clash royale
class Person:
    player_tag: str
    text_client: SmsAlert
    cell_number: int
    last_battle_time: datetime
    name: str

    def __init__(self, player_tag: str, cell_number: int, name: str = None, last_battle_time=None):
        self.player_tag = player_tag
        self.cell_number = cell_number
        self.text_client = SmsAlert(to=self.cell_number)
        self.text_client.config_from_file(config_path="twilio_config/twilio.txt")
        self.name = name
        self.last_battle_time = last_battle_time

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
