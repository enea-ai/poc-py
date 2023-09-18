import os
import yaml
import json

def checkDefined(name, value):
    if value is None:
        raise ValueError("'%s' is not defined" % name)
    
def read_yaml_file(filePath):
    with open(filePath, 'r') as file:
        data = yaml.safe_load(file)
    return data


def read_json_file(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
    return data