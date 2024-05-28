#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = 'Brown'):
        self.name = name

    def name(self, name):
        if(type(name) in (str)) and (1 <= len(name) <= 25):
            print("f{name}")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

        name = property()


