import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as file:  # TODO реализовать конвертер из csv в json
        temp_list = []
        for i, row in enumerate(file):
            data = row.strip(new_line).split(delimiter)
            if i == 0:
                headers = data
                continue

            temp_list.append(dict())

            for i, _ in enumerate(headers):
                temp_list[-1][headers[i]] = data[i]

    return temp_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
