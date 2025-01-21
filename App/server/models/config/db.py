import sqlite3

class DatabaseConnection:
    def __init__(self) -> None:
        self.sqliteConnection = sqlite3.connect('books.db')
        
    def getDatabaseConnection(self):
        return self.sqliteConnection