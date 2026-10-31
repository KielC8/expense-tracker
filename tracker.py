# Project: Expense Tracker
# Installment 5: The Menu Comes Alive
# Author: Ezekiel Cyrus D. Cuison
# Section: DIT 3-7
# Description: Tracks expenses using an interactive menu and evaluates budget status.

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\t\tKnow where your money goes.")
print("=" * 40)

name = input("\nWhat's your name? ")
tax_percent = int(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}! Let's track your expenses.")

subtotal = 0
count = 0

while True:
    print("\nMAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses\t\t(coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total

        print("-" * 40)
        print("SUMMARY")
        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal}")
        print(f"Tax ({tax_percent:.1f}%):\t${tax}")
        print(f"Grand total:\t${total}")

        if total > budget:
            print(f"Over budget by ${total - budget}!")
        elif total > budget * 0.90:
            print(f"Careful: only ${left} left.")
        else:
            print(f"Within budget. ${left} left.")

        print("-" * 40)

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Ezekiel Cyrus D. Cuison  |  Installment 5")
        break

    else:
        print("  Please choose 1, 2, 3 or 4.")