from base_sql import Base
from sqlalchemy import Column, String, BigInteger
import factory


class PlayerModel(Base):
    __tablename__ = "players"

    id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=False)
    place = Column(String, nullable=False)
    xp = Column(BigInteger, nullable=True)


class PlayerFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: "%s" % n)
    username = factory.Faker("name")
    place = factory.Faker("place")
    xp = factory.Faker("xp")

    class Meta:
        model = PlayerModel


PlayerFactory.create()
