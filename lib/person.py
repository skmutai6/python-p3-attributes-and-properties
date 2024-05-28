#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = 'Bruno', job = 'ITC'):
        self._name = name
        self._job = job

    def get_name(self):
        print({self.name})
        return self.name
    
    def set_name(self, name):
        if(type(name) in (str) and (1 <= len(name) <= 25)):
            print('f{name}')
            self.name = name
        

