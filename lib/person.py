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
    def __init__(self):
        self._name = name
        self._job = job

    def get_name(self):
        return self._name
    
    def get_job(self):
        return self._job
    
    def set_name(self, name):
        if(type(name)== str and (name < 25)):
            self._name = name.title()
        else:
            return 'Name must be string under 25 characters.'
    name = property(get_name, set_name)

    def set_job(self, job):
        if(job in APPROVED_JOBS):
            self._job = job
        else:
            return 'The job must be in the following list of jobs: '+ str(APPROVED_JOBS)
