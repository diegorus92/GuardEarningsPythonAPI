from pymongo import MongoClient

class Database:
    def __init__(self):
        self._db = self._get_guard_earnings2_database(self._connect_database())

    def _connect_database(self):
        connection = MongoClient('localhost', 27017)
        return connection

    def _get_guard_earnings2_database(self, connection):
        database = connection.guard_earnings2
        return database

    def get_database_context(self):
        return self._db