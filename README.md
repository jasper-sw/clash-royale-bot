# clash-royale-bot
This is a mulitpurpose bot / api wrapper for the official supercell clash royale api that allows you to monitor player data and respond in real time to events that take place in game. Actions available include texting your friends annoying messages when they lose games and congradulations when they win.

Supercell clash royale docs:
https://developer.clashroyale.com/#/documentation

# Requirements
- a supercell clash royale developer account and api token is needed to use this bot, you can make one for free at https://developer.clashroyale.com
- a twilio account, SID, token, and from number is also required if you want to send text messages to friends in response to in game events. You can create a free trial account to send texts at https://www.twilio.com/
- ensure you have python installed on the system where you intend to run the bot
# Setup and configuration
- clone this repo
- install the dependencies by running:
```
pip3 install -r requirements.txt
```
- create a folder called 'token_config/' in the root directory and create a file called 'token_config/api-tokens.txt' in that directory. In that file you can add one or more supercell clash royale api tokens formatted as follows:
```
my_token=[sample_token]

my_other_token=[sample_token2]
```
## The following steps are only necessary if you want to text people messages about their clash games
- create another folder called 'twilio_config/' in the root directory and include a file called 'twilio_config/twilio.txt' in that directory. In that file you need to include your twilio account details if you want to text people. Format the file as follows:
```
SID: [your twilio SID]
TOKEN: [your twilio token]
FROM: [your twilio from number]
```
 
 - finally, create a file called 'people.txt' in the root directory and format it as follows:
 ```
  {"person1": {"cell_number": [number1],"tag": "[clash royale tag1]"},"person2": {"cell_number":  [number2],"tag": "[clash royale tag2]"},"person3":{"cell_number": [number3],"tag":"[clash royale tag3]"}}
```
You can include as many people as you'd like to annoy here but please be mindful of requests and bandwidth to the supercell api.

## Final step
- with configuration complete just run navigate to the root directory and run:
```
python3 main.py
```
This will start the bot and leave it running until you kill the process.
