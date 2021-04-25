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
        assert type(plant) == Plant, 'Must be type Plant'
        if plant.get_name() in self._plants:
            del self._plants[plant.get_name()]

    def __contains__(self, plant):
        assert type(plant) == Plant, 'Must by type Plant'
        return plant.get_name() in self._plants

    def to_dict(self):
        """
        Converts the entire class into a dictionary representation.
        """

        temp = {
            'username' : self._username,
            'plants' : [p.to_dict for p in self._plants.values()]
        }
        return temp
        

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

    def to_dict(self):
        """
        Converts the entire class into a dictionary representation.
        """

        temp = {
            'name' : self._name,
            'type' : self._type,
            'last watered' : self._last_watered,
            'date registered' : self._date_registered
        }
        return temp


class AccountDatabase:
    """
    So and so database.
    """

    record = 'data/db_data.json'

    def __init__(self):
        # Account._name (str) : Account (Account)
        self._data = {}

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
    
    def has_account_by_name(acctname):
        return acctname in self._data

    def get_account_by_name(acctname):
        return self._data.get(acctname, '')

    def write_file(fname=record):
        with open(fname, 'w') as f:
            json.dump(fname, f)

    def read_file(fname=record):
        data = {}
        with open(fname, 'r') as f:
            data = json.load(f)
        return data


if __name__ == '__main__':
    plant_a = Plant('bob', 'pine tree')
    print(plant_a.to_dict())
    plant_a.water()
    print(plant_a.to_dict())

