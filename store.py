# You are a shop owner. You sell crab burgers. FOR MONEY!
# You have a few items. You want to sell them.
# Have an interface where someone can do the following things:
#
# x See what items you have for sale and their cost
# x Buy an item (their money goes down) [item goes out of stock once bought]
# * Check their balance and their inventory
# * Sell an item (their money goes up, but not as much as what they bought it for!)
# * Leave the store (or try anyway)
""" YO, MEATBAG! INSTALL PICK!"""

from pick import pick

"""
    1) Create dictionary of stuff with prices (Store front)
    2) Create a dictionary for user to check what they have and how much money left
    3)
"""

# Create an inventory of items, using a dictionary
customer_acc = 101
customer_inventory = {}

store_acc = 10000
store_inventory = {
    "Apple": 9999,
    "Babana": 500,
    "Scooter": 0.50,
    "Sword": 100,
    "House Rent": 100000000,
}


def show_inventory(inventory):
    for item_presentation in inventory:
        # When you loop through a dictionary, it loops through the "keys"
        # value = some_dictionary[key]

        # item_presentation = "Apple"
        # want 9999
        # store_inventory["Apple"] -> 9999
        # store_inventory[item_presentation] -> price
        price = inventory[item_presentation]
        print(item_presentation, "%.2f" % (price), sep=": $")
        # print(item_presentation + ": $" + price)
        # Apple: $9999

    # Pause to let the user look :D
    input()


# print("SOME PEOPLE CALL IT A TRASH, I CALL IT A GARBAGE!")
title = "WELCOME TO BOB'S BUYOUT!"
print("SOME PEOPLE CALL IT A TRASH, I CALL IT A GARBAGE!")
options = ["See what is in the store", "Show what I got", "Buy something", "Go Home"]
while customer_acc != 0:
    print("WHAT'CHA WANT?!")

    option, index = pick(options, title)

    if index == 0:
        show_inventory(store_inventory)
    elif index == 1:
        show_inventory(customer_inventory)
    elif index == 2:
        # ->>> show_inventory(store_inventory)
        title = "WHAT'CHA WANT TO BUY?!"

        counter = []
        items = list(store_inventory.items())
        for name, price in items:
            counter.append("%s: $%.2f" % (name, price))

        counter, index = pick(counter, title)
        name, price = items[index]

        print("BE MI GUST!")

        customer_acc -= price
        customer_inventory[name] = price / 2
        store_acc += price
        store_inventory.pop(name)
    else:
        print("GO AWAY AND NEVER COME BACK!")
        break

# TODO: Show how much money is had when you show an inventory
# TODO: Don't let you buy things you can't afford!!!
