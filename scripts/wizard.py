import random
from datetime import datetime


def date_to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day


HOUSES = ["🔴 Гриффиндор", "🟢 Слизерин", "🟡 Пуффендуй", "🔵 Когтевран"]
WAND_TYPES = "сердечная жила дракона, перо феникса, волос единорога".split(
    ", ")
PATRONUS = "персидский кот, рысь, выдра, козёл, феникс, заяц, полосатая кошка, кабан, олень, лань, горностай, терьер, лебедь, сущность в виде гномика, капибара, неведома зверюшка, человек".split(", ")


class Wizard:
    def __init__(self, user_id: int) -> None:

        datestring = date_to_integer(datetime.now().date())
        random.seed(user_id + datestring)

        self.wand_size = self.get_wand_size()
        self.wand_type = self.get_wand_type()
        self.house = self.get_house()
        self.muggle_percent = self.get_muggle_percent()
        self.patronus = self.get_patronus()

    def get_wand_size(self):
        return random.randint(1, 29)

    def get_house(self):
        return random.choice(HOUSES)

    def get_wand_type(self):
        return random.choice(WAND_TYPES)

    def get_muggle_percent(self):
        return random.randint(0, 99)

    def get_patronus(self):
        return random.choice(PATRONUS)

    def __str__(self) -> str:
        return (
            f"Длина моей палочки - {self.wand_size}см, {self.wand_type}\n"
            f"Я на {self.muggle_percent}% маггл\n"
            f"Мой факультет - {self.house}\n"
            f"Патронус - {self.patronus.capitalize()}"
        )


