import json
import ast
import pandas as pd


def iterate_till_next_index(string, start_pos, search_for):
    if string[start_pos] in [search_for, '}', ' ']:
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


def convert_txt_to_excel(location):
    with open(location, 'r', encoding="utf8") as file:
        lines = file.readlines()
    list_linse = ast.literal_eval(lines[0])
    new_list = []
    for index, each_entry in enumerate(list_linse):
        try:
            new_list.append(convert((each_entry)))
        except Exception as err:
            print('error while parsing entry at index: ' + str(index) + ' : ', each_entry)
    df = pd.DataFrame(new_list)
    df.to_excel("output2.xlsx")
    print('Success')
    return 'Success'


convert_txt_to_excel('./myCases.txt')
