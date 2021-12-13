import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from models.model import Base


class NotSuchTaskException(Exception):
    pass


class MysqlClient:

    def __init__(self, user, password, db_name, host='127.0.0.1', port=3306):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host
        self.port = port

        self.connection = None
        self.session = None
        self.engine = None

    def connect(self, db_created=True):
        db_name = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db_name}'

        self.engine = sqlalchemy.create_engine(url, encoding='utf8')
        self.connection = self.engine.connect()

        self.session = sessionmaker(bind=self.connection.engine)()

    def recreate_db(self):
        self.connect(db_created=False)

        self.execute_query(f'DROP database IF EXISTS {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)

        self.connection.close()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_all_tables(self):
        for i in range(1, 6):
            self.create_task_table(i)

    def create_task_table(self, task_id):
        if task_id == 1:
            table_name = 'unique_requests'
        elif task_id == 2:
            table_name = 'requests_stats'
        elif task_id == 3:
            table_name = 'top_10_most_frequent'
        elif task_id == 4:
            table_name = 'top_5_request_by_body_bytes_sent_with_4xx_status_code'
        elif task_id == 5:
            table_name = 'top_5_users_by_requests_count_with_5xx_status_code'
        else:
            raise NotSuchTaskException(f'Task{task_id} not found!')

        if not inspect(self.engine).has_table(table_name):
            Base.metadata.tables[table_name].create(self.engine)
