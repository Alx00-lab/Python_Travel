from models import User, Asset, Transaction

# Crear transacciones
transact = Transaction("TX003", 2, 150.0, "2025-07-14")
transact1 = Transaction("TX003", 4, 100.0, "2025-07-14")
print(f"Total calculado: {transact.total_value()}")

# Crear activos
active = Asset("BTC", "Bitcoin", 5000.0)
active1 = Asset("PTC", "Platinium Coin", 3000.0)

# Actualizar precio
active.updateAsset(5500.0)
print(f"Asset Value: {active.actualPrice}")

# Crear usuario y agregar transacciones
user1 = User("A001", "Alex", "alex@example.com")
user1.add_Transact(transact)
user1.add_Transact(transact1)


print(f"Actual Transacción: {len(user1.transactions)}, Total acumulado: {user1.total_portfolio()}")
