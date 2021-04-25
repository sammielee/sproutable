# db.py

from datetime import date
import json


class Account:
    """
    Represents a user and all of their plants
    """

    def __init__(self, acctname):
        self._username = acctname
        # Plant._name (str) : Plant (Plant)
        self._plants = {}

    def get_username(self):
        return self._username

    def add_plant(self, plant):
        assert type(plant) == Plant, 'Must be type Plant.'
        self._plants[plant.get_name()] = plant

    def remove_plant(self, plant):
        assert type(plant) == Plant, 'Must be type Plant.'
        if plant.get_name() in self._plants:
            del self._plants[plant.get_name()]

    def __contains__(self, plant):
        assert type(plant) == Plant, 'Must by type Plant.'
        return plant.get_name() in self._plants

    @staticmethod
    def to_dict(account):
        """
        Converts the entire class into a dictionary representation.
        """

        assert type(account) == Account, 'Must be type Account.'
        temp = {
            'username' : account._username,
            'plants' : [p.to_dict for p in account._plants.values()]
        }
        return temp

    @staticmethod
    def from_dict(d):
        """
        Converts an applicable dictionary into an Account object.
        """
    
        try:
            acct = Account(d['username'])
            for plant_d in d['plants']:
                acct.add_plant(Plant(plant_d))
        except e:
            raise e
        return acct
        
        

class Plant:
    """
    Representative of a plant.
    """

    def __init__(self, name, ptype):
        self._name = name
        self._type = ptype

        # '_last_watered' is a date string
        self._last_watered = 'Never'
        self._date_registered = date.today().isoformat()

    def water(self):
        self._last_watered = date.today().isoformat()

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_last_watered(self):
        return self._last_watered

    def get_data_registered(self):
        return self._date_registered

    @staticmethod
    def to_dict(plant):
        """
        Converts the entire class into a dictionary representation.
        """

        assert type(plant) == Plant, 'Must be type Plant.'
        temp = {
            'name' : self._name,
            'type' : self._type,
            'last watered' : self._last_watered,
            'date registered' : self._date_registered
        }
        return temp

    @staticmethod
    def from_dict(d):
        """
        Converts an applicable dictionary into a Plant object.
        """

        try:
            plant = Plant(d['name'], d['type'])
            plant._last_watered = d['last watered']
            plant._date_registered = d['date registered']
        except e:
            print(e)
            raise e
        return plant


class AccountDatabase:
    """
    So and so database.
    """

    record = 'data/db_data.json'

    def __init__(self, record=None):
        # Account._name (str) : Account (Account)
        self._data = {}
        self._record = record if record != None else AccountDatabase.record

    def add_account(self, account):
        assert type(account) == Account, 'Must be type Account.'
        self._data[account.get_username()] = account

    def remove_account(self, account):
        assert type(account) == Account, 'Must be type Account.'
        if account.get_username() in self._data:
            del self._data[account.get_username()]

    def __contains__(self, account):
        assert type(account) == Account, 'Must be type Account.'
        return account.get_username() in self._data
    
    def has_account_by_name(self, acctname):
        return acctname in self._data

    def get_account_by_name(self, acctname):
        return self._data.get(acctname, '')

    def remove_account_by_name(self, acctname):
        del self._data[acctname]

    def write_file(self):
        with open(self._record, 'w') as f:
            json.dump(self._data, f, default=lambda o : Account.to_dict(o))

    def read_file(self):
        with open(self._record, 'r') as f:
            self._data = json.load(f)


data = AccountDatabase()
