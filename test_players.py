import pytest

from player_sql import Player
from base_sql import Session


@pytest.fixture(scope="function")
def session(connection):
    session = Session(bind=connection)
    session = Session()
    yield session
    session.close()


# @pytest.fixture(scope="function")
def player_func():
    player = Player(username="zoo", place="2nd", xp=23654)
    print(player)
    return player


def my_func_to_delete_Player(session, Player_id):
    session.query(Player).filter(Player.id == Player_id).delete()


def test_case(session, monkeypatch):
    test_request_payload = {"username": "something", "place": "2nd", "xp": 23654}
    # player = Player(username="zoo", place="2nd", xp=23654)
    # monkeypatch.setattr(player)
    # Player = session.add(player)
    # assert session.query(Player).one()
    player1 = session.add(player_func())
    # assert session.query(player1).one()
    my_func_to_delete_Player(session, Player.id)

    result = session.query(Player).one_or_none()
    assert result is None
