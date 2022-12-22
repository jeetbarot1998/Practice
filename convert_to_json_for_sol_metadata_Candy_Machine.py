import os
import shutil
import json
import random

json_format = {
    "name": "Lunar Baby #1",
    "symbol": "LB",
    "description": "Lunar Baby",
    "image": "0.png",
    "attributes": [ {
"type":"rat"
    }],
    "properties": {
        "files": [
            {
                "uri": "0.png",
                "type": "image/png"
            }
        ]
    }
} 


def make_png_json(editions, json_tempelate, nft_name, symbol = None ,creator = None ,collection = None, description=None):
    for val in range(0,editions):
        json_location = os.getcwd() + '/assets/' + str(val) + '.json'
        with open(json_location,"w+") as file:
            temp = json_tempelate.copy()
            temp['name'] =  f"{nft_name} #{str(val)}"
            temp['symbol'] = f"{str(symbol)}"
            temp['description'] = f"{str(description)}"
            temp['image'] = f"{str(val)}.png"
            # temp['edition'] = val
            temp['properties']['files'][0]['uri'] = f"{str(val)}.png"
            temp['properties']['creators'][0]['address'] = str(creator)
            temp['collection']['name'] = str(collection)
            file.write(json.dumps(temp))
            file.close()
        src_dir = os.getcwd() + '\\0' + '.png'
        dest_dir = os.getcwd()+"/assets/" + str(val) + '.png'
        shutil.copy(src_dir,dest_dir)
        #copy the file to destination dir
        

# make_png_json(125, json_format,'Test Cap','Test Cap', '56izEsShAiLTzdruzTe3zy9nuAhWXd2RjRXGE7UbQjdc', 'Test', 'Cap' )


json_format2 = {
    "name": "Lunar Baby #1",
    "symbol": "LB",
    "description": "Lunar Baby",
    "image": "0.png",
    "attributes": [ {
    "type":"rat"
    }],
    "properties": {
        "files": [
            {
                "uri": "0.png",
                "type": "image/png"
            }
        ]
    }
}

def make_png_json2(json_tempelate, nft_name, copies_of_each_nft=2):
    li = list(range(0,12*copies_of_each_nft))
    # li = list(range(0,24))
    iter_li= []
    li_copy = list(range(0,12*copies_of_each_nft))
    # li_copy = list(range(0,24))
    file_name = 0
    nfts_names_list = ['dog','dragon','gallo','goat','horse','monkey','ox','pig','rabbit','rat','snake','tiger']
    for ind, _ in enumerate(li):
        id_to_populate = random.choice(li_copy)
        print('choice==',id_to_populate)
        li_copy.remove(id_to_populate)
        if (ind%copies_of_each_nft == 0):
            if len(iter_li) == 0:
                iter_li.append(0)
                file_name = nfts_names_list[0]
            else:
                iter_li.append(iter_li[len(iter_li) - 1] + 1)
                file_name = nfts_names_list[iter_li[iter_li[len(iter_li) - 1]]]
        print(file_name)
        json_location = os.getcwd() + '/assets/' + str(id_to_populate) + '.json'
        with open(json_location, "w+") as file:
            temp = json_tempelate.copy()
            temp['name'] = f"{nft_name} #{str(id_to_populate)}"
            temp['image'] = f"{str(id_to_populate)}.png"
            temp['attributes'][0]['type'] = f"{file_name}"
            temp['properties']['files'][0]['uri'] = f"{str(id_to_populate)}.png"
            file.write(json.dumps(temp))
            file.close()
            
        src_dir = os.getcwd() + "/lunar baby toys/" + f"{file_name}" + '.jpg'
        dest_dir = os.getcwd() + "/assets/" + str(id_to_populate) + '.png'
        shutil.copy(src_dir,dest_dir)



make_png_json2(json_format2, 'Lunar Baby', 125)
