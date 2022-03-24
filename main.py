# importing the requests library
from dateutil import parser
from datetime import timezone
from entity_classes.person import Person
import sys
import time
sys.path.append(".")

my_api_token = """eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2N
hNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM5NTQzMDMxLTAyMzctNDQ5OS05MWZkLTI4NmFlZDZ
hNmI0MSIsImlhdCI6MTY0NzkxODE3OCwic3ViIjoiZGV2ZWxvcGVyLzFlNDMyMmNlLTYzZjYtMWMwNi05NGQ1LWM5MDY1ZWUxZDcwYyIsInNjb3BlcyI
6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI2Ny4xNj
kuMjQyLjE4OCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.b2sfTkBuer_8_od7VEbAW9aSmzZtV492JOMSbyjHkUTfvevFf8uqG1k_Jq5Pav0XU54mlgrL
5jU1SlOgHAYhxg"""

jasper = Person(api_token=my_api_token, cell_number=8015108393, player_tag="#LCJ8RPLPR")
john = Person(api_token=my_api_token, cell_number=8017122161, player_tag="#Y08P2PRLP")
hayden = Person(api_token=my_api_token, cell_number=3852144611, player_tag="#QJQU0J89C")
justin = Person(api_token=my_api_token, cell_number=8019277910, player_tag="#QJVPGPLGG")

people = [jasper, john, hayden, justin]


not_done = True
print("Starting ClashBot")
while not_done:
    time.sleep(0.5)

    for homie in people:
        elapsed = homie.client.get_time_since_last_battle()
        # if elapsed.total_seconds() < 100:
        #     print(elapsed.total_seconds())
        if elapsed.total_seconds() < 100:
            last_battle = homie.client.get_last_battle_info()
            crown_count = last_battle["team"][0]["crowns"]
            last_battle_time = last_battle["battleTime"]

            last = parser.parse(last_battle_time).astimezone(timezone.utc)
            first = parser.parse(homie.last_battle_info["battleTime"]).astimezone(timezone.utc)
            elapsed = last - first

            if elapsed.total_seconds() > 0:
                homie.last_battle_info = last_battle
                if list(last_battle["team"][0].keys()).__contains__("trophyChange"):
                    trophy_change = last_battle["team"][0]["trophyChange"]
                    if trophy_change < 0:
                        win = False
                    else:
                        win = True
                    message = crown_message(crown_count=crown_count, win=win)
                    print("Sent text to [{}] with message: [{}]".format(homie, homie.cell_number))

                    text = SendAlert.SmsAlert(to=homie.cell_number)
                    text.config_from_file(config_path="twilio_config/twilio.txt")
                    text.send_message(message=message)
                elif not list(last_battle["team"][0].keys()).__contains__("trophyChange"):
                    win = False
                    message = crown_message(crown_count=crown_count, win=win)
                    print("Sent text to [{}] with message: [{}]".format(homie, message))

                    homie.text_client.send_message(message=message)


