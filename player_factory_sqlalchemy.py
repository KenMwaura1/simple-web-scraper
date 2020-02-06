from base_sql import Base, Session
from sqlalchemy import Column, String, BigInteger
import factory

session = Session()


class PlayerModel(Base):
    __tablename__ = "players-table"

    id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=False)
    place = Column(String, nullable=False)
    xp = Column(String, nullable=True)


class PlayerFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: "%s" % n)
    username = factory.Faker("name")
    place = factory.Faker("name")
    xp = factory.Faker("email")

    class Meta:
        model = PlayerModel
