import pytest

from player_sql import Player
from player_factory_sqlalchemy import PlayerFactory
from player_factory_basic import PlayerModel
from base_sql import Session

session = Session()


@pytest.fixture(scope="function")
def session(connection):
    transaction = connection.begin()
    session = Session(bind=connection)
    PlayerFactory._meta.sqlalchemy_session = session  # NB: This line added
    yield session
    session.close()
    transaction.rollback()


def my_func_to_delete_Player(session, Player_id):
    session.query(PlayerModel).filter(PlayerModel.id == Player_id).delete()


def test_case(session):
    Player = PlayerFactory.create()
    assert session.query(PlayerModel).one()

    my_func_to_delete_Player(session, Player.id)

    result = session.query(PlayerModel).one_or_none()
    assert result is None
