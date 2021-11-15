import argparse
import json
import os.path
import re


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--json',
        action='store_true',
        default=False,
        dest='json_flag'
    )
    parser.add_argument(
        '--path',
        default=os.path.join(os.path.curdir, 'access.log'),
        dest='path_to_log'
    )
    args = parser.parse_args()

    return args.json_flag, args.path_to_log


def parse_log(log_line):
    return re.search(
        r'(?P<remote_addr>[.\d]*) - (?P<remote_user>.*) \[(?P<local_time>.*)] \"(?P<request>.*)\" ' +
        r'(?P<response_status>\d\d\d) (?P<body_bytes_sent>\d*|-) \"(?P<http_referer>.*)\" ' +
        r'\"(?P<http_user_agent>.*)\" \"(?P<http_x_forwarded_for>.*)\"',
        log_line
    ).groupdict()


def parse_request(log_request):
    return re.search(r'(?P<method>.*) (?P<url>\S*) (?P<headers>.*)', log_request).groupdict()


def write(result_dict):
    with open(OUTPUT_FILE_NAME + '.txt', 'w') as file:
        for name, data in result_dict.items():
            file.write(name + '\n')
            for dict in data:
                for key, value in dict.items():
                    file.write(f'{str(key)}={str(value)}; ')

                file.write('\n')
            file.write('\n')

    if JSON_FLAG:
        with open(OUTPUT_FILE_NAME + '.json', 'w') as file:
            json.dump(result_dict, file, indent=4)


JSON_FLAG, PATH = get_options()
OUTPUT_FILE_NAME = 'python_result'

result = {}

unique_requests_dict = {}
all_requests_parsed = []

with open(PATH, 'r') as log_file:
    for line in log_file:
        parsed_line = parse_log(line)

        request = parsed_line['request']
        unique_requests_dict[request] = unique_requests_dict.get(request, 0) + 1

        all_requests_parsed.append(parsed_line)

result['UNIQUE REQUESTS'] = [{'COUNT': len(unique_requests_dict.keys())}]

reqs_methods = {}
for req in unique_requests_dict.keys():
    method = parse_request(req)['method']
    reqs_methods[method] = reqs_methods.get(method, 0) + 1
result['REQUESTS STATS'] = [{'METHOD': method, 'COUNT': count} for method, count in reqs_methods.items()]

result['TOP 10 MOST FREQUENT'] = [
    {'URL': parse_request(req[0])['url'], 'COUNT': req[1]}
    for req in sorted(unique_requests_dict.items(), key=lambda x: x[1], reverse=True)[:10]
]

result['TOP 5 REQUEST BY BODY BYTES SENT WITH 4XX STATUS CODE'] = [
    {
        'IP': top_request['remote_addr'],
        'STATUS': top_request['response_status'],
        'SIZE': top_request['body_bytes_sent'],
        'URL': parse_request(top_request['request'])['url'],
    }
    for top_request in sorted(
        [request for request in all_requests_parsed if request['response_status'].startswith('4')],
        key=lambda x: x['body_bytes_sent'], reverse=True)[:5]
]

top_users_req = {}
for request in [request for request in all_requests_parsed if request['response_status'].startswith('5')]:
    ip = request['remote_addr']
    top_users_req[ip] = top_users_req.get(ip, 0) + 1
result['TOP 5 USERS BY REQUESTS COUNT WITH 5XX STATUS CODE'] = [
    {'IP': ip, 'COUNT': count}
    for ip, count in sorted(top_users_req.items(), key=lambda x: x[1], reverse=True)[:5]
]

write(result)
