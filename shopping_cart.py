products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]
item_list = []
del_trans = []
i = 0
print("Scan the item and then enter the Quantity")
print("To Print the Receipt type 'DONE'")
print("To negate an entered transaction type 'DEL'")
while True:
    item = input("Transaction No." + str(i+1) + " - ")
    #check if input is "done", "del", a non-integer, an invalid product id, or valid
    if item.lower() == "done":
        break
    elif item.lower() == "del":
        try:
            void = int(input("Transaction number?"))
            if void >= 1 and void <= i-1 and void not in del_trans:
                item_list = [v for v in item_list if v['trans'] != void]
                del_trans.append(void)
            elif void in del_trans:
                print("Transaction has already been deleted")
            else:
                print("Invalid transaction number")
        except ValueError:
            print("Invalid transaction number")
    elif not item.isdigit():
        print("Invalid item number")
    elif not any(p['id'] == int(item) for p in products):
        print("Invalid item number")
    else:
        #the user enters a number, and if they do not the quantity is assumed to be 1
        try:
            quantity = int(input("Quantity - "))
        except ValueError:
            quantity = 1
        i += 1
        item_att = {
            "trans": i,
            "number": item,
            "quantity": quantity
        }
        item_list.append(item_att)

#function to create a dictionary for the final Receipt
def receipt_item(itemdict):
    idno = next(idn for idn in products if str(idn["id"]) == itemdict["number"])
    resultdict = {
        "name": idno["name"],
        "quantity": itemdict["quantity"],
        "price": idno["price"],
        "total": idno["price"]*itemdict["quantity"],
    }
    return resultdict

#printing of final receipt
print()
print()
print("RECEIPT")
print("--------------------")
subtotal = 0
for item in item_list:
    dict = receipt_item(item)
    subtotal += dict["total"]
    n = dict["name"]
    p = '${0:.2f}'.format(dict["price"])
    q = str(dict["quantity"])
    t = '${0:.2f}'.format(dict["total"])
    print(n + " - " + p + " x " + q + " = " + t)
print("--------------------")
tax = subtotal * .1
total = subtotal + tax
subtotal = '${0:.2f}'.format(subtotal)
print("Subtotal - " + subtotal)
tax = '${0:.2f}'.format(tax)
print("     Tax - " + tax)
total = '${0:.2f}'.format(total)
print("   Total - " + total)
