#Expense Tracker - Installment 3: tracker does math; Author: Ezekiel Cyrus D. Cuison
print("=" * 40)
print("EXPENSE TRACKER".center(40))
print("Know where your money goes.".center(40))
print("=" * 40)

print("\nMAIN MENU")
print("  [1] Add an expense".ljust(28) + "(coming soon)")
print("  [2] View all expenses".ljust(28) + "(coming soon)")
print("  [3] Show total spent".ljust(28) + "(coming soon)")
print("  [4] Exit".ljust(28) + "(coming soon)")

name = input("What's your name? ")
print("Welcome, " + name + "! Let's log two expenses.")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
print("  - " + item1 + ":\t$" + str(amount1))
print("  - " + item2 + ":\t$" + str(amount2))
print("Subtotal:\t$" + str(subtotal))
print("Average:\t$" + str(average))
print("Tax (" + str(tax_percent) + "%):\t$" + str(tax))
print("Grand total:\t$" + str(total))
print("Over budget?\t" + str(over_budget))
print("Left in budget:\t$" + str(left))
print("-" * 40)
print("Made by: Ezekiel Cyrus D. Cuison  |  Installment 3")