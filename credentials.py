import json

def get_credentials(json_filepath):
    with open(json_filepath, "r") as rjson:
        jfile = json.load(rjson)
        return jfile
