from flask_seeder import Seeder, Faker, generator
from app import db, app
from app import Request, Requisite
import random

card_number_list = []
for i in range(100):
    card_num = []
    for j in range(4):
        num = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        card_num.append(num)
    card_number_list.append('-'.join(card_num))

card_number_list_str = "(" + "|".join(card_number_list) + ")"



class RequestSeeder(Seeder):
    def run(self):
        faker = Faker(
            cls=Request,
            init={
                "card_number": generator.String(pattern=card_number_list_str),
                "cash_amount": generator.Integer(start=100, end=1000),
                "status": generator.String(pattern="(pending|approved|rejected")
            }
        )
        for _ in range(5000):
            db.session.add(faker.create())


class RequisiteSeeder(Seeder):
    def run(self):
        faker = Faker(
            cls=Requisite,
            init={
                "card_number": generator.String(card_number_list_str),
                "card_type": generator.String(pattern="(visa|mastercard|bank-order)"),
                "full_name": generator.Name(),
                "telephone_number": generator.String(pattern="89[0-9]{2}-[0-9]{3}-[0-9]{2}-[0-9]{2}"),
                "limit": generator.Integer(start=1000, end=5000)
            }
        )
        for _ in range(100):
            db.session.add(faker.create())


# Запуск сидера
app.app_context().push()
RequisiteSeeder().run()
RequestSeeder().run()
