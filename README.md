# clash-royale-bot
This is a mulitpurpose bot / api wrapper for the offical supercell clash royale api that allows you to monitor player data and respond in real time to events that take place in game. Actions available include texting your friends annoying messages when they lose games and congradulations when they win.

Supercell clash royale docs:
https://developer.clashroyale.com/#/login

# Setup
- clone this repo
- create a folder called 'token_config/' in the root directory and create a file called 'token_config/api-tokens.txt' in that directory. In that file you can add one or more supercell clash royale api tokens formatted as follows:
```
my_token=[sample_token]

my_other_token=[sample_token2]
```
## The following steps are only neccesary if you want to text people messages about their clash games
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
