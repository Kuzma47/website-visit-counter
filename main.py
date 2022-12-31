from website_database import WebsiteDB
from datetime import datetime
import sys


def get_new_date(date, year, month, day):
    return year * 365 + month * 30 + day \
           - (date[0] * 365 + date[1] * 30 + date[2])


def get_statistics(i):
    db = WebsiteDB()
    stat = list(map(lambda v: v[i], db.get_values()))
    d = {}
    for s in stat:
        if s not in d.keys():
            d[s] = 0
        d[s] += 1
    i = 1
    result = ""
    for item, count in reversed(sorted(d.items(), key=lambda v: v[1])):
        result += f'{i}. {item}: {count}\n'
        i += 1
    return result


def get_info(param):
    db = WebsiteDB()
    records = db.get_values()
    params_values = {"year": 365, "month": 31, "day": 1}
    if param != 'all' and param not in params_values.keys():
        raise AttributeError(f'{param} is not correct param.')
    data = []
    current_date = datetime.now()
    for row in records:
        diff = get_new_date(
            list(map(int, row[1].split()[0].split('-'))),
            current_date.year,
            current_date.month,
            current_date.day
        )
        if param == 'all' or diff <= params_values[param]:
            data.append(row)
    return data


def format_data(data):
    id_set = set(list(map(lambda d: d[0], data)))
    result = f'Visits count: {len(data)}\n'\
             f'Total users: {len(id_set)}\n'
    for row in data:
        result += '\t'.join(row) + '\n'
    return result


COMMANDS = {'b': 2, 'p': 3, 'r': 4, 'u': 0}


def get_result():
    if len(sys.argv) > 1:
        command = sys.argv[1][1:]
    else:
        command = None
    if command == 't':
        if len(sys.argv) > 2:
            time = sys.argv[2]
        else:
            time = '-all'
        return format_data(get_info(time[1:]))
    if command in COMMANDS.keys():
        return get_statistics(COMMANDS[command])


if __name__ == '__main__':
    print(get_result())
