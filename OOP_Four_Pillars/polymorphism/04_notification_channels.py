class EmailNotification:
    def __init__(self, address):
        self.address = address

    def send(self, message):
        return f"Email to {self.address}: {message}"

class SMSNotification:
    def __init__(self, number):
        self.number = number

    def send(self, message):
        return f"SMS to {self.number}: {message}"

def notify(channel, message):
    print(channel.send(message))

notify(EmailNotification("student@example.com"), "Quiz tomorrow")
notify(SMSNotification("03000000000"), "Lab tomorrow")
