import factory

from .base_sql import Session

session = Session()


class Player:
    def __init__(self, username, place, xp):
        self.place = place
        self.username = username
        self.xp = xp


class PlayerFactory(factory.Factory):
    username = factory.Faker("name")
    place = factory.Faker("email")
    xp = factory.Faker("email")

    class Meta:
        model = Player


PlayerFactory.build()
