from models.model import Task1, Task2, Task3, Task4, Task5
from utils.log_parser import LogParser
from static_variables import MAX_URL_LENGTH, MAX_METHOD_LENGTH


class Builder:

    def __init__(self, client, parser):
        self.client = client
        self.parser: LogParser = parser

    def create_task1_data(self):
        if self.parser.unique_requests_dict != {}:
            task1 = Task1(count=len(self.parser.unique_requests_dict.keys()))
            self.client.session.add(task1)
        self.client.session.commit()

    def create_task2_data(self):
        reqs_methods = {}
        for req in self.parser.unique_requests_dict.keys():
            method = self.parser.parse_request(req)['method']
            reqs_methods[method] = reqs_methods.get(method, 0) + 1

        for method, count in reqs_methods.items():
            task2_entry = Task2(method=method[:MAX_METHOD_LENGTH], count=count)
            self.client.session.add(task2_entry)
        self.client.session.commit()

    def create_task3_data(self):
        for req in sorted(self.parser.unique_requests_dict.items(), key=lambda x: x[1], reverse=True)[:10]:
            task3_entry = Task3(
                url=self.parser.parse_request(req[0])['url'][:MAX_URL_LENGTH],
                count=req[1]
            )
            self.client.session.add(task3_entry)
        self.client.session.commit()

    def create_task4_data(self):
        for top_request in sorted(
                [request for request in self.parser.all_requests_parsed if request['response_status'].startswith('4')],
                key=lambda x: x['body_bytes_sent'], reverse=True)[:5]:
            task4_entry = Task4(
                ip=top_request['remote_addr'],
                status_code=top_request['response_status'],
                sent_size=top_request['body_bytes_sent'],
                url=self.parser.parse_request(top_request['request'])['url'][:MAX_URL_LENGTH]
            )
            self.client.session.add(task4_entry)
        self.client.session.commit()

    def create_task5_data(self):
        top_users_req = {}
        for request in [request for request in self.parser.all_requests_parsed
                        if request['response_status'].startswith('5')]:
            ip = request['remote_addr']
            top_users_req[ip] = top_users_req.get(ip, 0) + 1

        for ip, count in sorted(top_users_req.items(), key=lambda x: x[1], reverse=True)[:5]:
            task5_entry = Task5(ip=ip, count=count)
            self.client.session.add(task5_entry)
        self.client.session.commit()
