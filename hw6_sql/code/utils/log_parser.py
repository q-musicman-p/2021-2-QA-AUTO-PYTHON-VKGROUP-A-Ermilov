import re


class LogParser:

    def __init__(self, path):
        self.path = path
        self.unique_requests_dict = {}
        self.all_requests_parsed = []

    @staticmethod
    def parse_line(log_line):
        return re.search(
            r'(?P<remote_addr>[.\d]*) - (?P<remote_user>.*) \[(?P<local_time>.*)] \"(?P<request>.*)\" ' +
            r'(?P<response_status>\d\d\d) (?P<body_bytes_sent>\d*|-) \"(?P<http_referer>.*)\" ' +
            r'\"(?P<http_user_agent>.*)\" \"(?P<http_x_forwarded_for>.*)\"',
            log_line
        ).groupdict()

    @staticmethod
    def parse_request(log_request):
        return re.search(r'(?P<method>.*) (?P<url>\S*) (?P<headers>.*)', log_request).groupdict()

    def parse(self):
        with open(self.path, 'r') as log_file:
            for line in log_file:
                parsed_line = self.parse_line(line)

                request = parsed_line['request']
                self.unique_requests_dict[request] = self.unique_requests_dict.get(request, 0) + 1

                self.all_requests_parsed.append(parsed_line)
