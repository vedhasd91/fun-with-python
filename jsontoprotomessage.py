#!/usr/bin/python

#########################
# Convert JSON to PROTO 
# definition
#########################

import json

def main():
    with open("test.json") as in_file:
        json_obj = json.load(in_file)
        print json_obj
        for key in json_obj:
            print key + " is " + str(type(json_obj[key]))

if __name__ == "__main__":
    main()