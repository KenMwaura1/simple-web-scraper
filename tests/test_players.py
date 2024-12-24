import pytest

from db.player_sql import Player
from db.top_earning_players_sql import Earning_Player
from db.base_sql import Session, engine, Base

from db.player_factory_basic import PlayerFactory


@pytest.fixture
def player_func():
    return PlayerFactory.build()


@pytest.fixture
def player_func2():
    return PlayerFactory.build()

def test_player(session, player_func):
    session.add(player_func)
    assert session.query(Player)
    my_func_to_delete_Player(session, Player.id)
    result = session.query(Player).one_or_none()
    assert result is None

def test_player2(session, player_func2):
    session.add(player_func2)
    assert session.query(Earning_Player)
    my_func_to_delete_Player2(session, Earning_Player.id)
    result = session.query(Earning_Player).one_or_none()
    assert result is None


@pytest.fixture(scope="module")
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


#
@pytest.fixture(scope="function")
def session(connection):
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()


@pytest.fixture(scope="function")
def session(connection):
    session = Session(bind=connection)
    session = Session()
    yield session
    session.close()


@pytest.fixture(scope="function")
def player_func():
    player = Player(username="zoo", place="2nd", xp=23654)
    print(player)
    return player


@pytest.fixture(scope="function")
def player_func2():
    player = Earning_Player(username="zoo", place="2nd", earnings=23654)
    print(player)
    return player


def my_func_to_delete_Player(session, Player_id):
    session.query(Player).filter(Player.id == Player_id).delete()


def my_func_to_delete_Player2(session, Player_id):
    session.query(Earning_Player).filter(Earning_Player.id == Player_id).delete()


def test_case(session, monkeypatch):
    test_request_payload = {"username": "something", "place": "2nd", "xp": 23654}
    session.add(Player(username="zoo", place="2nd", xp=23654))
    assert session.query(Player)
    monkeypatch.setattr("db.player_sql.Player", test_request_payload)
    my_func_to_delete_Player(session, Player.id)
    result = session.query(Player).one_or_none()
    assert result is None

def test_case2(session, monkeypatch):
    test_request_payload = {"username": "something", "place": "2nd", "earnings": 23654}
    session.add(Earning_Player(username="zoo 2", place="2nd", earnings=23654))
    assert session.query(Earning_Player)
    monkeypatch.setattr("db.top_earning_players_sql.Earning_Player", test_request_payload)
    my_func_to_delete_Player2(session, Earning_Player.id)
    result = session.query(Earning_Player).one_or_none()
    assert result is None

def test_player(session, player_func):
    session.add(player_func)
    assert session.query(Player)
    my_func_to_delete_Player(session, Player.id)
    result = session.query(Player).one_or_none()
    assert result is None


def test_player2(session, player_func2):
    session.add(player_func2)
    assert session.query(Earning_Player)
    my_func_to_delete_Player2(session, Earning_Player.id)
    result = session.query(Earning_Player).one_or_none()
    assert result is None
