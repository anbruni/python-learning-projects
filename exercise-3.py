# You're given two dictionaries: a product inventory and a shipment of new stock. Write code that:

# Merges the shipment into the inventory (add quantities for existing items, add new items)
# Removes any item whose final quantity is 0 or less
# Finds the item with the highest quantity in the final inventory

inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 10,
    "grapes": 5,
    "mangoes": 15,
}

shipment = {
    "bananas": 20,
    "oranges": -10,
    "kiwis": 40,
    "grapes": -5,
    "strawberries": 25,
}

# # Your code here:
# # 1. Merge shipment into inventory (update existing, add new)
for item in shipment:
    if item in inventory:
        inventory[item] += shipment[item]
    else:
        inventory[item] = shipment[item]

def my_filtering_function(pair):
    key, value = pair
    if value > 0:
        return True
    else:
        return False
 
inventory = dict(filter(my_filtering_function, sorted(inventory.items())))

max = 0
product = ""
for item in inventory:
    if inventory[item] > max:
        max = inventory[item]
        product = item
    
print(f"the max item is {product} with {max} units")
# # 2. Remove items with quantity <= 0
# # 3. Find and print the item with the highest quantity
# #
# # Expected output:
# #   Updated inventory: {'apples': 50, 'bananas': 50, 'kiwis': 40, 'strawberries': 25, 'mangoes': 15}
# #   Most stocked item: apples (50)
# Rules:

# Do not use max() with a key= argument — find the maximum yourself with a loop.
# Modify inventory in place (don't create a new dict for the merge).
# For removing items, be careful: think about whether you can remove from a dict while looping over it.
