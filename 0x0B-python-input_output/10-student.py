#!/usr/bin/python3
''' module: 10-student
'''


class Student:
    '''class: student
    '''

    def __init__(self, first_name, last_name, age):
        '''method: __init__
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''method: to_json
        '''
        full_dict = {}
        for key, value in self.__dict__.items():
            full_dict[key] = value
        keys = list(full_dict.keys())
        if attrs is not None:
            for key in keys:
                if key not in attrs:
                    del full_dict[key]
        return full_dict
