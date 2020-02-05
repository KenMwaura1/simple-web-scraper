import factory


class Player:
    def __init__(self, username, place, xp):
        self.place = place
        self.username = username
        self.xp = xp


class PlayerFactory(factory.Factory):
    username = factory.Faker("name")
    place = factory.Faker("place")
    xp = factory.Faker("xp")

    class Meta:
        model = Player


PlayerFactory.build()
