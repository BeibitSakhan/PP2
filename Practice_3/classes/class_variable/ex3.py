class Ticket:
    VALID_ZONES = ["A", "B", "C"]  # Список зон

    def __init__(self, zone):
        if zone in Ticket.VALID_ZONES:
            self.zone = zone
        else:
            print("Ошибка: такой зоны нет!")

# Usage
t = Ticket("D")  # Ошибка