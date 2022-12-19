import json
import ast


def iterate_till_next_index(string, start_pos, search_for):
    if string[start_pos] in [search_for, '}']:
        return start_pos
    else:
        return iterate_till_next_index(string, start_pos + 1, search_for)


def convert(potential_invld_dct):
    try:
        k = json.loads(potential_invld_dct)
        return k
    except Exception as err:
        end_loc = iterate_till_next_index(potential_invld_dct, err.__dict__['pos'], ',')
        potential_invld_dct = potential_invld_dct[:err.__dict__['pos'] - 1] + '"' + potential_invld_dct[err.__dict__['pos']: end_loc] + \
            '"' + potential_invld_dct[end_loc:]
        return convert(potential_invld_dct)


val = '{"a":"b", "c": wrong, "d":"e", "f": pppp}'
print(convert(val))


import pandas as pd
with open('./myCases.txt', 'r' , encoding="utf8") as file:
    lines = file.readlines()
list_linse = ast.literal_eval(lines[0])
new_list = []
for index, each_entry in enumerate(list_linse):
    try:
        new_list.append(json.loads((each_entry)))
    except Exception as err:
        print('error while parsing entry at index: ' + str(index) + ' : ', each_entry)
df = pd.DataFrame(new_list)
df.to_excel("output2.xlsx")