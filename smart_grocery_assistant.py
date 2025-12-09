# Smart Grocery Shopping Assistant - Basic Menu
import datetime as dt

# Data storage (in-memory)
grocery_list = []   # current items the user wants to buy
purchase_history = []
inventory = []

# Rule base: healthier alternatives for certain items
HEALTHIER_ALTERNATIVES = {
    "white bread": "brown bread",
    "full cream milk": "low fat milk",
    "sugar": "brown sugar",
    "instant noodles": "whole wheat pasta",
    "soft drink": "sparkling water"
}

STAPLE_ITEMS = ["milk", "bread", "eggs", "rice", "oil"]

# Shelf life for expiry reminders (in days)
SHELF_LIFE = {
    "milk": 1,
    "bread": 3,
    "eggs": 14,
    "yogurt": 10,
    "chicken": 3,
    "rice": 180,
    "oil": 365
}

def print_header(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def view_grocery_list():
    print_header("Current Grocery List")

    # If list is empty, say so
    if len(grocery_list) == 0:
        print("Your grocery list is empty.")
        return

    # Show items one by one
    for index, item in enumerate(grocery_list, start=1):
        print(f"{index}. {item}")



def add_item_to_grocery_list():
    print_header("Add Item to Grocery List")

    item = input("Enter the item you want to add: ").strip().lower()

    if item == "":
        print("You did not enter anything.")
        return

    # Check if the item has a healthier alternative
    if item in HEALTHIER_ALTERNATIVES:
        alternative = HEALTHIER_ALTERNATIVES[item]
        print(f"Suggestion: A healthier option for '{item}' is '{alternative}'.")
        choice = input("Do you want to replace it with the healthier option? (y/n): ").strip().lower()

        if choice == "y":
            item = alternative
            print(f"Using healthier option: {item}")

    grocery_list.append(item)
    print(f"'{item}' has been added to your grocery list.")



def mark_items_purchased():
    print_header("Mark Items as Purchased")

    if len(grocery_list) == 0:
        print("Your grocery list is empty. Add items first.")
        return

    # Show items
    for index, item in enumerate(grocery_list, start=1):
        print(f"{index}. {item}")

    choices = input("\nEnter item numbers to mark as purchased (e.g., 1,3): ").strip()

    if choices == "":
        print("No items selected.")
        return

    selected = []

    # Parse input like "1,2,4"
    for part in choices.split(","):
        part = part.strip()
        if part.isdigit():
            n = int(part)
            if 1 <= n <= len(grocery_list):
                selected.append(grocery_list[n-1])

    if len(selected) == 0:
        print("No valid selections.")
        return

    # Process each purchased item
    for item in selected:
        purchase_history.append({
            "name": item,
            "date": dt.date.today()
        })

        expiry_date = get_expiry_date(item)

        inventory.append({
            "name": item,
            "purchase_date": dt.date.today(),
            "expiry_date": expiry_date
        })

        print(f"Purchased '{item}'. Expiry date: {expiry_date}")

        grocery_list.remove(item)  # remove from list


def smart_suggestions():
    print_header("Smart Suggestions (Rule-Based)")

    if len(purchase_history) == 0:
        print("No previous purchases detected. Suggestions cannot be generated yet.")
        return

    today = dt.date.today()
    suggestions = []

    # Rule 1: Items bought 5–9 days ago
    for entry in purchase_history:
        name = entry["name"]
        days_ago = (today - entry["date"]).days

        if 5 <= days_ago <= 9 and name not in grocery_list:
            if name not in suggestions:
                suggestions.append(name)

    # Rule 2: Staples not bought for 14+ days
    for staple in STAPLE_ITEMS:
        last = find_last_purchase(staple)

        if last is None:
            # User never bought this staple
            suggestions.append(staple)
        else:
            days_ago = (today - last["date"]).days
            if days_ago > 14 and staple not in grocery_list:
                suggestions.append(staple)

    if len(suggestions) == 0:
        print("No suggestions at the moment.")
        return

    # Show suggestions and ask whether to add them
    print("Based on your past purchases, you might need:")

    for item in suggestions:
        last = find_last_purchase(item)
        if last:
            days_ago = (today - last["date"]).days
            print(f"- {item} (last bought {days_ago} days ago)")
        else:
            print(f"- {item} (common staple item)")

    # Ask user to add each suggested item
    for item in suggestions:
        choice = input(f"Add '{item}' to your grocery list? (y/n): ").strip().lower()
        if choice == "y":
            grocery_list.append(item)
            print(f"Added: {item}")


def check_expiry_reminders():
    print_header("Expiry Reminders")

    if len(inventory) == 0:
        print("You have no items in your inventory.")
        return

    today = dt.date.today()
    alert_found = False

    for item in inventory:
        name = item["name"]
        expiry = item["expiry_date"]

        days_left = (expiry - today).days

        if days_left < 0:
            print(f"⚠️ ALERT: '{name}' expired {-days_left} days ago! (Expiry was: {expiry})")
            alert_found = True
        elif days_left <= 2:
            print(f"⚠️ Warning: '{name}' will expire in {days_left} day(s) (Expiry: {expiry})")
            alert_found = True

    if not alert_found:
        print("✔ All items are fresh. Nothing is close to expiry.")


def view_purchase_history():
    print_header("Purchase History")

    if len(purchase_history) == 0:
        print("No purchases recorded yet.")
        return

    for entry in purchase_history:
        name = entry["name"]
        date = entry["date"]
        print(f"- {name} (purchased on {date})")

def get_expiry_date(item_name):
    days = SHELF_LIFE.get(item_name.lower(), 7)
    return dt.date.today() + dt.timedelta(days=days)

def find_last_purchase(item_name):
    item_name = item_name.lower()

    past = [p for p in purchase_history if p["name"].lower() == item_name]

    if len(past) == 0:
        return None

    # Sort by newest date
    past.sort(key=lambda x: x["date"], reverse=True)
    return past[0]

def main():
    print_header("Smart Grocery Shopping Assistant")
    print("Welcome!")

    while True:
        print_header("Main Menu")
        print("1. View grocery list")
        print("2. Add item to grocery list")
        print("3. Mark items as purchased")
        print("4. Get smart suggestions")
        print("5. Check expiry reminders")
        print("6. View purchase history")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_grocery_list()
        elif choice == "2":
            add_item_to_grocery_list()
        elif choice == "3":
            mark_items_purchased()
        elif choice == "4":
            smart_suggestions()
        elif choice == "5":
            check_expiry_reminders()
        elif choice == "6":
            view_purchase_history()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




