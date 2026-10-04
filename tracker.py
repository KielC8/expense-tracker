#Expense Tracker - Installment 2; Author: Ezekiel Cyrus D. Cuison
print("=" * 40)
print("\t     EXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("  [1] Add an expense".ljust(28) + "(coming soon)")
print("  [2] View all expenses".ljust(28) + "(coming soon)")
print("  [3] Show total spent".ljust(28) + "(coming soon)")
print("  [4] Exit".ljust(28) + "(coming soon)")

name = input("What's your name? ")
print("Welcome, " + name + "! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print("  -", item1, ":", "$", amount1)
print("  -", item2, ":", "$", amount2)
print("Total spent:", "$", total)
print("Average:", "$", average)
print("-" * 40)
print("Made by: Ezekiel Cyrus D. Cuison  |  Installment 2")