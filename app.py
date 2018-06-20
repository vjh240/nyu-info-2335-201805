import csv
import os
import getpass

def menu(username, products_count):
    print("""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    """)
    print("Welcome " + username + "!")
    print("There are " + products_count + " products in the database.")
    print("""
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
    """)

def read_products_from_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print("READING PRODUCTS FROM FILE: " + filepath)
    products = []
    productstemp = []
    with open(filepath) as csv_file:
        productstemp = csv.DictReader(csv_file)
        for row in productstemp:
            products.append(row)
    return products

def write_prices_to_file(filename,products):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
        writer.writeheader()
        for d in products:
            row = {
                "id": d["id"],
                "name": d["name"],
                "aisle": d["aisle"],
                "department": d["department"],
                "price": d["price"]
            }
            writer.writerow(row)

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)

def follow_up():
    while True:
        userchoice = input("Would you like to perform another operation? (Y/N)  ")
        if userchoice.lower() == "y":
            yes_or_no = True
            break
        elif userchoice.lower() == "n":
            yes_or_no = False
            break
        else:
            print("Invalid Answer")
    return yes_or_no

def run():
    products = read_products_from_file("products_test.csv")
    username = getpass.getuser()
    itemcount = "1"
    while True:
        menu(username,itemcount)
        userchoice = input("Please select an operation: ")
        if userchoice.lower() == "list":
            for product in products:
                print(product["id"] + " - " + product["name"])
            answer = follow_up()
            if answer == True:
                print()
            else:
                break
        elif userchoice.lower() == "show": #input validation
            userchoice = input("Enter the ID of the product you wish to see more about - ")
            idno = next(idn for idn in products if str(idn["id"]) == userchoice)
            print()
            print("Item# - " + idno["id"])
            print("Name  - " + idno["name"])
            print("Dept. - " + idno["department"])
            print("Aisle - " + idno["aisle"])
            print("Price - " + idno["price"])
            print()
            answer = follow_up()
            if answer == True:
                print()
            else:
                break
        elif userchoice.lower() == "create":#input validation
            i = {}
            idno = [idno["id"] for idno in products]
            idno = list(map(int, idno))
            idno.sort(key=int,reverse=True)
            i["id"] = str(idno[0]+1)
            print("Item# - " + i["id"])
            i["name"] = input("Name  - ")
            i["department"] = input("Dept. - ")
            i["aisle"] = input("Aisle - ")
            i["price"] = input("Price - ")
            print(i)
            products.append(i)
            i = ""
            answer = follow_up()
            if answer == True:
                print()
            else:
                break
        elif userchoice.lower() == "update":#input validation on product id and attribute to update
            userchoice = input("Enter the ID of the product you wish to update - ")
            update_item = [d for d in products if d['id'] == userchoice]
            products = [d for d in products if d['id'] != userchoice]
            update_item = update_item[0]
            print("Name  - " + update_item["name"])
            print("Dept  - " + update_item["department"])
            print("Aisle - " + update_item["aisle"])
            print("Price - " + update_item["price"])
            userchoice = input("Which attribute would you like to change? ")
            if userchoice.lower() == "name":
                userchoice = input("New Value - ")
                update_item["name"] = userchoice
            elif userchoice.lower() == "dept":
                userchoice = input("New Value - ")
                update_item["department"] = userchoice
            elif userchoice.lower() == "aisle":
                userchoice = input("New Value - ")
                update_item["aisle"] = userchoice
            elif userchoice.lower() == "price":
                userchoice = input("New Value - ")
                update_item["price"] = userchoice
            else:
                print("Invalid entry")
            products.append(update_item)
            answer = follow_up()
            if answer == True:
                print()
            else:
                break
        elif userchoice.lower() == "destroy":#input validation
            userchoice = input("Enter the ID of the product you wish to delete - ")
            products = [d for d in products if d['id'] != userchoice]
            print(products)
            answer = follow_up()
            if answer == True:
                print()
            else:
                break
        else:
            print()
            print("Invalid operation")
    print()
    print("Okay! Thanks for using the app and have a nice day.")
    print()

    write_prices_to_file("products_test.csv",products)
    # Finally, save products to file so they persist after script is done...
    #write_products_to_file(products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
