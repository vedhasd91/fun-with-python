#!/usr/bin/python

#########################
# Convert JSON to PROTO 
# definition
#########################

import json

def openbrace(in_str):
    return str(in_str)+' {'

def closebrace(in_str):
    return str(in_str)+'\n}'

def messagecreate():
    return 'message'

def typedetermine(json_obj):
    out_str_ = 
    for key in json_obj:
        print key + " is " + str(type(json_obj[key]))
        if isinstance(json_obj[key],int):
        elif isinstance(json_obj[key],float):
        elif isinstance(json_obj[key],str):
        elif isinstance(json_obj[key],list):
        elif isinstance(json_obj[key],dict):
    return

def main():
    with open("test.json") as in_file:
        json_obj = json.load(in_file)
        print json_obj
        typedetermine(json_obj)
    return       

if __name__ == "__main__":
    main()