class Phone:
    def call(self, number):
        print(f"Звоню по номеру {number}...")

class SmartPhone(Phone):
    def browse_internet(self):
        print("Открываю браузер...")

# Смартфон умеет и звонить (от родителя), и заходить в интернет
iphone = SmartPhone()
iphone.call("911")
iphone.browse_internet()