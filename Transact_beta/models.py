from datetime import datetime
class User:
    def __init__(self, userID: str, name: str, email: str, transactions: list["Transaction"]| None = None):
        self.userID = userID
        self.name = name
        self.email = email
        self.transactions = transactions if transactions is not None else []
        
    def add_Transact(self, transaction: "Transaction") -> float:
        if isinstance(transaction, Transaction):
            self.transactions.append(transaction)
            print(f"Transaction added: {transaction}")
        else:
            print("Error: Transaction must be an object of class Transaction.")
    
    def total_portfolio(self):
        total = 0
        for transct in self.transactions:
            total += transct.total_value()
        return total
    
    
    def __repr__(self):
        return f"ID='{self.userID}', User(Name='{self.name}', Email='{self.email}', Transactions='{self.transactions}')"


# Asset class
class Asset:
    def __init__(self, simbol: str, name: str, actualPrice: float):
        self.simbol = simbol
        self.name = name
        self.actualPrice = actualPrice
    
    def updateAsset(self, new_Price: float) -> None:
        if new_Price > 0:
            self.actualPrice = new_Price
            print(f"Actual price updated: {new_Price}")
        else:
            print("Error: new price must be greater than 0")

    def __repr__(self) -> str:
         return f"Asset(Simbol={self.simbol}, Name={self.name}, ActualPrice={self.actualPrice})"


# Trassaction class
class Transaction:
    def __init__(self, transactID: str, cant: int, price: float, date: datetime):
        self.transactID = transactID
        self.cant = cant
        self.price = price
        self.date = date
    
    def total_value(self) -> float:
        return self.cant * self.price
    
    def __repr__(self):
        return f"Transaction(ID={self.transactID}, cant={self.cant}, price={self.price}, date='{self.date}')"

#End         

