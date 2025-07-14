from models import User, Asset, Transaction

transact = Transaction("TX003", 2, 150.0, "2025-07-14")
transact1 = Transaction("TX004", 4, 100.0, "2025-07-14")
print(f"Total calculado: {transact.total_value()}")

# Update Asset
active = Asset("BTC", "Bitcoin", 5000.0)
active.updateAsset(5500.0)
print(F"Asset Value: {active.actualPrice}")

# Check out User Get transactions

user1 = User("A001", "Alex", "alex@example.com")
user1.add_Transact(transact)

user2 = User("A002", "Maria", "Maria@example.com")
user2.add_Transact(transact1)

total_Transact = transact.total_value() + transact1.total_value()

print(f"Actual Transacion: {len(user1.transactions + user2.transactions)}")