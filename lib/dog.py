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
    def __init__(self):
        self._name = name
        self._breed = breed

    def get_name(self):
        return self._name
    
    def get_breed(self):
        return self._breed
    
    def set_name(self, name):
        if(type(name)== str and (1 >= name <= 25)):
            self._name = name
        else:
            return 'Name must be string between 1 and 25 characters.'
    name = property(get_name, set_name)

    def set_breed(self, breed):
        if(breed in APPROVED_BREEDS):
            self._breed = breed
        else:
            return 'The breed must be in the following list of dog breeds: '+ str(APPROVED_BREEDS)