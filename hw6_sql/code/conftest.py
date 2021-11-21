import pytest
from mysql.client import MysqlClient
from utils.log_parser import LogParser


def pytest_addoption(parser):
    parser.addoption('--path', default='access.log')


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    log_parser = LogParser(config.getoption('--path'))

    if not hasattr(config, 'workerinput'):
        mysql_client.recreate_db()
    mysql_client.connect()

    if not hasattr(config, 'workerinput'):
        mysql_client.create_all_tables()
        log_parser.parse()

    config.mysql_client = mysql_client
    config.log_parser = log_parser


@pytest.fixture(scope='session')
def log_parser(request) -> LogParser:
    return request.config.log_parser


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()
