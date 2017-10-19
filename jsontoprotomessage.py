#!/usr/bin/python

import json




def main():
    with open("test.json") as in_file:
        json_obj = json.load(in_file)
        print json_obj



if __name__ == "__main__":
    main()
