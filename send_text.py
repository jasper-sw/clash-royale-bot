from twilio.rest import Client


# a class to send texts to phone numbers
class SmsAlert:
    recipient: str = None
    sender: str
    body: str
    sid: str
    token: str
    config_path: str

    def __init__(self, to="", sender="", body="", sid="", token=""):
        self.recipient = to
        self.sender = sender
        self.body = body
        self.sid = sid
        self.token = token

    # reads class config from a .txt file
    # format file like so:
    # SID: xxxxxxxxxxxxxxxxxxxxxxxxx
    # TOKEN: xxxxxxxxxxxxxxxxxxxxxxx
    # FROM: +1xxxxxxxxxx
    # TO: +1xxxxxxxxxx
    def config_from_file(self, config_path):
        if not config_path.endswith('.txt'):
            print("\nERROR: config file is not .txt, please resolve\n")
            return
        self.config_path = config_path
        self.import_config()

    def print_config(self):
        print("\n--SMS Config--")
        print("Recipient: {}\nSender: {}\nSID: {}\nToken: {}\nConfig file: {}".format
              (self.recipient, self.sender, self.sid, self.token, self.config_path))

    # ensure we have the necessary twilio variables to continue
    def fully_configured(self):
        if self.config_path == "":
            return False
        if self.sid == "":
            return False
        if self.sender == "":
            return False
        if self.token == "":
            return False

        return True

    # get twilio config variables from twilio_config/twilio.txt
    def import_config(self):
        with open(self.config_path) as file:
            for line in file:
                line_arr = line.split()
                if line_arr[0] == 'SID:':
                    self.sid = line_arr[1]
                if line_arr[0] == 'TOKEN:':
                    self.token = line_arr[1]
                if line_arr[0] == 'FROM:':
                    self.sender = line_arr[1]
                if self.fully_configured():
                    return

    def send_message(self, message):
        if self.recipient is None:
            raise SystemExit("SmsAlert: ERROR: You forgot to set the text message recipient!")
        sms_client = Client(self.sid, self.token)
        sms_client.messages.create(
            to=self.recipient,
            from_=self.sender,
            body=message)

