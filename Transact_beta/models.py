class User:
    def __init__(self, Id, name, email):
        self.Id = Id
        self.name = name
        self.email = email


# Asset class
class Asset:
    def __init__(self, simbol, name, actualPrice):
        self.simbol = simbol
        self.name = name
        self.actualPrice = actualPrice


# Trassaction class
class Trassaction:
    def __init__(self, transactID, cant, price, date):
        self.transactID = transactID
        self.cant = cant
        self.price = price
        self.date = date
