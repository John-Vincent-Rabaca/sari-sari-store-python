#Sari-sari Store py
def print_category(category):
    if category == "Noodles":
        for noodle in categories["Noodles"]:
            print(noodle)
    elif category == "Canned Products":
        for noodle in categories["Canned Products"]:
            print(noodle)
    elif category == "Biscuits":
        for noodle in categories["Biscuits"]:
            print(noodle)
    elif category == "Beverages":
        for noodle in categories["Beverages"]:
            print(noodle)
    elif category == "Shampoo & Conditioners":
        for noodle in categories["Shampoo & Conditioners"]:
            print(noodle)
    elif category == "Laundry Products":
        for noodle in categories["Laundry Products"]:
            print(noodle)


categories = {
    "Noodles": {"lucky me": 11.00, 
                "pancit-canton": 16.00}, 
    "Canned Products": {}, 
    "Biscuits": {}, 
    "Beverages": {}, 
    "Shampoo & Conditioners": {}, 
    "Laundry Products": {}
}

for category in categories:
    print(category)

category = input("\nChoose a category: ").title()
print()

print_category(category)
    
item = input("\nItem: ")
print(f"Price for {item} is: {categories[category][item]}")