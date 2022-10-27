#!/usr/bin/env python3
'''for peer learning serialization and deserialization using JSON import'''
import json

'''Complex data type'''
class Peers(object):
    '''Peer class'''
    def __init__(self, first_name=None, last_name=None, country=None):
        '''initialize Peers'''
        self.last_name = last_name
        self.first_name = first_name
        self.country = country

    def intro(self):
        '''Print Instance Attributes'''
        print(self.first_name, self.last_name, self.country)

    def to_json_string(self):
        '''Serilaize Instance into JSON formatted string''' 
        return json.dumps(self.__dict__)

    def load_json_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            original = json.load(f)
            return original

    def save_json_to_file(self, filename):
        '''Saves instance of Peer in a file'''
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f)

    def __str__(self):
        '''formatted printing of instance'''
        return "fname: {} | lname: {} | country: {}".format(self.first_name, self.last_name, self.country)

