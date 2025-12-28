#Sari-sari Store py

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

if category == "Noodles":
    for noodle in categories["Noodles"]:
        print(noodle)
elif category == "Noodles":
    for noodle in categories["Noodles"]:
        print(noodle)
elif category == "Noodles":
    for noodle in categories["Noodles"]:
        print(noodle)
elif category == "Noodles":
    for noodle in categories["Noodles"]:
        print(noodle)
elif category == "Noodles":
    for noodle in categories["Noodles"]:
        print(noodle)
elif category == "Noodles":
    for noodle in categories["Noodles"]:
        print(noodle)
    
item = input("\nItem: ")
print(f"Price for {item} is: {categories[category][item]}")