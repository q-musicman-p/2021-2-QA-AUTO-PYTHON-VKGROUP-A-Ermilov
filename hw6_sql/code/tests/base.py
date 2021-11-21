import pytest

from models.model import Task1, Task2, Task3, Task4, Task5
from mysql.client import MysqlClient, NotSuchTaskException
from utils.builder import Builder


class BaseTest(object):


    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client, log_parser):
        self.mysql_client: MysqlClient = mysql_client
        self.builder: Builder = Builder(client=mysql_client, parser=log_parser)


    def get_result_task(self, task_id):
        self.mysql_client.session.commit()

        if task_id == 1:
            return self.mysql_client.session.query(Task1).all()
        elif task_id == 2:
            return self.mysql_client.session.query(Task2).all()
        elif task_id == 3:
            return self.mysql_client.session.query(Task3).all()
        elif task_id == 4:
            return self.mysql_client.session.query(Task4).all()
        elif task_id == 5:
            return self.mysql_client.session.query(Task5).all()
        else:
            raise NotSuchTaskException(f'Task{task_id} not found!')