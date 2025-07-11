class User:
    def __init__(self, userID: int, name: str, email: str):
        self.userID = userID
        self.name = name
        self.email = email
        self.transactions = []
        
    def add_Transact(self, transaction):
        if isinstance(transaction, Transaction):
            self.transactions.append(transaction)
            print(f"Transaction added: {transaction}")
        else:
            print("Error: Transaction must be an object of class Transaction.")
    
    def __repr__(self):
        return f"ID='{self.userID}', User(Name='{self.name}', Email='{self.email}', Transactions='{self.transactions}')"


# Asset class
class Asset:
    def __init__(self, simbol: str, name: str, actualPrice: float):
        self.simbol = simbol
        self.name = name
        self.actualPrice = actualPrice
    
    def updateAsset(self, new_Price: float):
        if new_Price > 0:
            self.actualPrice = new_Price
            print(f"Actual price updated: {new_Price}")
        else:
            print("Error: new price must be greater than 0")

    def __repr__(self):
         return f"Asset(Simbol={self.simbol}, Name={self.name}, ActualPrice={self.actualPrice})"


# Trassaction class
class Transaction:
    def __init__(self, transactID: str, cant: int, price: float, date):
        self.transactID = transactID
        self.cant = cant
        self.price = price
        self.date = date
    
    def total_value(self) -> float:
        return self.cant * self.price
    
    def __repr__(self):
        return f"Transaction(ID={self.transactID}, cant={self.cant}, price={self.price}, date='{self.date}')"

#End         

user1 = User(1, "Alex", "Alex@exmaple.com")

# Create a Asset 
activo = Asset("BTC", "Bitcoin", 30000.0)

# Updated Asset
activo.updateAsset(4000.0)

# Print 
print(activo)

# Create transct

t1 = Transaction("TX1001", 2, 25.50, "2025-07-11")
t2 = Transaction("TX1002", 4, 100.00, "2025-07-12")

total = t1.total_value() + t2.total_value()

print(f"Total of both transactions: {total}")

# Add transact to user
user1.add_Transact(t1)
user1.add_Transact(t2)

# Show me data

print(user1)