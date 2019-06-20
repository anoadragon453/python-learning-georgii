# You are a shop owner. You sell crab burgers. FOR MONEY!
# You have a few items. You want to sell them.
# Have an interface where someone can do the following things:
#
# x See what items you have for sale and their cost
# * Buy an item (their money goes down) [item goes out of stock once bought]
# * Check their balance and their inventory
# * Sell an item (their money goes up, but not as much as what they bought it for!)
# * Leave the store (or try anyway)

"""
    1) Create dictionary of stuff with prices (Store front)
    2) Create a dictionary for user to check what they have and how much money left
    3)
"""
# Create an inventory of items, using a dictionary
print("WELCOME TO BOB'S BUYOUT!")
print("SOME PEOPLE CALL IT A TRASH, I CALL IT A GARBAGE!")
store_inventory = {
    "Apple": 9999,
    "Babana": 500,
    "Scooter": 0.50,
    "Sword": 100,
    "House Rent": 100000000,
}

for item_presentation in store_inventory:
    # When you loop through a dictionary, it loops through the "keys"
    # value = some_dictionary[key]

    # item_presentation = "Apple"
    # want 9999
    # store_inventory["Apple"] -> 9999
    # store_inventory[item_presentation] -> price
    price = store_inventory[item_presentation]
    print(item_presentation, "%.2f" % (price), sep=": $")
    # print(item_presentation + ": $" + price)
    # Apple: $9999

# print("SOME PEOPLE CALL IT A TRASH, I CALL IT A GARBAGE!")

print("WHAT'CHA WANT?!")
user_input = input()
if user_input == "See your inventory":
    # print("SOME PEOPLE CALL IT A TRASH, I CALL IT A GARBAGE!")
    # print(store_inventory)
    pass
else:
    print("GO AWAY AND NEVER COME BACK!")
