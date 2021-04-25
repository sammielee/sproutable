# File: logging.py


import datetime


class Entry:

    threshold = datetime.timedelta(hours=4)

    def __init__(self, acctname, time=datetime.datetime.today()):
        self._username = acctname
        self._recent = time

    def get_username(self):
        return self._username

    def difference(self, other=datetime.datetime.today()):
        return other - self._recent

    def log_time(self):
        self._recent = datetime.datetime.today()

    def is_overdue(self):
        return self.difference() > Entry.threshold


