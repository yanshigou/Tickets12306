"""Train tickets query via CLI

Usage:
  ticket [-dgktz] <from> <to> <date>

Options:
  -h --help     Show this screen.
  --version     Show version.
  -d            动车
  -g            高铁
  -k            快速
  -t            特快
  -z            直达
"""
from collections import OrderedDict
import requests
import urllib3
from datetime import datetime
from docopt import docopt
import stations
from colorama import Fore
from prettytable import PrettyTable

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TrainCollection(object):
    headers = '车次 车站 时间 历时 商务座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座 其他'.split()

    def __init__(self, raw_trains, options):
        self.raw_trains = raw_trains
        self.options = options

    def colored(self, color, string):
        return ''.join([getattr(Fore, color.upper()), string, Fore.RESET])

    def get_from_to_station_name(self, data_list):
        from_station_telecode = data_list[6]
        to_station_telecode = data_list[7]
        return "\n".join([self.colored('green', stations.get_name(from_station_telecode)),
                        self.colored('red', stations.get_name(to_station_telecode))])

    def get_start_arrive_time(self, data_list):
        return '\n'.join([
            self.colored('green', data_list[8]),
            self.colored('red', data_list[9])
            ])

    def parse_train_data(self, data_list):
        return {
            "station_train_code": data_list[3],
            "from_to_station_name": self.get_from_to_station_name(data_list),
            "start_arrive_time": self.get_start_arrive_time(data_list),
            "lishi": data_list[10],
            "business_class_seat":data_list[32] or '--',
            "first_class_seat":data_list[31] or '--',
            "second_class_seat":data_list[30] or '--',
            "super_soft_sleep":data_list[21] or '--',
            "soft_sleep":data_list[23] or '--',
            "dong_sleep":data_list[33] or '--',
            "hard_sleep":data_list[28] or '--',
            "soft_seat":data_list[24] or '--',
            "hard_seat":data_list[29] or '--',
            "no_seat":data_list[26] or '--',
            "other":data_list[22] or '--'
        }

    def need_print(self, data_list):
        station_train_code = data_list[3]
        initial = station_train_code[0].lower()
        return (not self.options or initial in self.options)

    @property
    def trains(self):
        for train in self.raw_trains:
            data_list = train.split('|')
            if self.need_print(data_list):
                yield self.parse_train_data(data_list)

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.headers)
        for train in self.trains:
            pt.add_row([
                train["station_train_code"],
                train["from_to_station_name"],
                train["start_arrive_time"],
                train["lishi"],
                train["business_class_seat"],
                train["first_class_seat"],
                train["second_class_seat"],
                train["super_soft_sleep"],
                train["soft_sleep"],
                train["dong_sleep"],
                train["hard_sleep"],
                train["soft_seat"],
                train["hard_seat"],
                train["no_seat"],
                train["other"]
                ])
        print(pt)

class Cli(object):
    url_template = (
        'https://kyfw.12306.cn/otn/leftTicket/query?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT')

    def __init__(self):
        self.arguments = docopt(__doc__, version='Tickets 1.1')
        self.from_station = stations.get_telecode(self.arguments['<from>'])
        self.to_station = stations.get_telecode(self.arguments['<to>'])
        self.date = self.arguments['<date>']
        self.check_arguments_validatity()
        self.options = ''.join([key for key, value in self.arguments.items() if value is True ])

    @property
    def request_url(self):
        return self.url_template.format(self.date, self.from_station, self.to_station)

    def check_arguments_validatity(self):
        if self.from_station is None or self.to_station is None:
            print('请输入有效车站名称')
            exit()
        try:
            if datetime.strptime(self.date, '%Y-%m-%d') < datetime.now():
                raise ValueError
        except:
            print('请输入有效日期')
            exit()

    def run(self):
        r = requests.get(self.request_url, verify=False)
        trains = r.json()['data']['result']
        TrainCollection(trains, self.options).pretty_print()

if __name__ == '__main__':
    Cli().run()

# def cli():
   
#     arguments = docopt(__doc__, version='Tickets 1.0')
#     from_station = stations.get_telecode(arguments.get('<from>'))
#     to_station = stations.get_telecode(arguments.get('<to>'))
#     date = arguments.get('<date>')
#     options = ''.join(
#         [key for key, value in arguments.items() if value is True])
#     url = ('https://kyfw.12306.cn/otn/leftTicket/query?'
#             'leftTicketDTO.train_date={}&'
#             'leftTicketDTO.from_station={}&'
#             'leftTicketDTO.to_station={}&'
#             'purpose_codes=ADULT').format(date, from_station, to_station)

#     r = requests.get(url, verify=False)
#     raw_trains = r.json()['data']['result']
#     pt = PrettyTable()
#     pt._set_field_names('车次 车站 时间 历时 商务座 一等座 二等座 高级软卧 软卧 硬卧 软座 硬座 无座 其他'.split())
#     for raw_train in raw_trains:
#         data_list = raw_train.split('|')
#         train_no = data_list[3]
#         initial = train_no[0].lower()
#         if not options or initial in options:
#             from_station_code = data_list[6]
#             to_station_code = data_list[7]
#             start_time = data_list[8]
#             arrive_time = data_list[9]
#             time_duration = data_list[10]
#             business_class_seat = data_list[32] or '--'
#             first_class_seat = data_list[31] or '--'
#             second_class_seat = data_list[30] or '--'
#             super_soft_sleep = data_list[21] or '--'
#             soft_sleep = data_list[23] or '--'
#             hard_sleep = data_list[28] or '--'
#             soft_seat = data_list[24] or '--'
#             hard_seat = data_list[29] or '--'
#             no_seat = data_list[26] or '--'
#             other = data_list[22] or '--'
#             pt.add_row([
#                 train_no,
#                 '\n'.join([Fore.GREEN + stations.get_name(from_station_code) + Fore.RESET, Fore.RED + stations.get_name(to_station_code) + Fore.RESET]),
#                 '\n'.join([Fore.GREEN + start_time + Fore.RESET, Fore.RED + arrive_time + Fore.RESET]),
#                 time_duration,
#                 business_class_seat,
#                 first_class_seat,
#                 second_class_seat,
#                 super_soft_sleep,
#                 soft_sleep,
#                 hard_sleep,
#                 soft_seat,
#                 hard_seat,
#                 no_seat,
#                 other
#                 ])
#     print(pt)

# if __name__ == '__main__':
#     main()