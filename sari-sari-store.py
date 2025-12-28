#Sari-sari Store py
def print_category(category, categories):
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

def main():
    categories = {
        "Noodles": {"lucky me": 11.00, 
                    "nissin ramen": 16.00,
                    "pancit canton": 16.00
                    }, 
        "Sauces & Seasonings": {"crispy fry": 1.00, 
                                "del monte tomato ketchup bottle": 1.00,
                                "fish sauce sottle": 1.00,
                                "fish sauce sachet": 1.00,
                                "mang tomas bottle": 1.00, 
                                "mang tomas sachet": 1.00,
                                "silver swan soy sauce sachet": 1.00,
                                "silver swan vinegar sachet": 1.00,
                                "soy sauce bottle": 1.00,
                                "soy sauce sachet": 1.00,
                                "tasty boy": 1.00,
                                "ufc banana ketchup bottle": 1.00,
                                "ufc banana ketchup sachet": 1.00,
                                "vinegar bottle": 1.00,
                                "vinegar sachet": 1.00
                                },
        "Canned Products": {"555 carne norte": 1.00,
                            "555 tuna": 1.00, 
                            "alaska classic evaporated filled milk": 1.00,
                            "alaska condensada large": 1.00, 
                            "alaska condensada small": 1.00,
                            "alaska evaporada large": 1.00,
                            "alaska evaporada small": 1.00,
                            "angel condensada large": 1.00,
                            "angel condensada small": 1.00,
                            "angel evaporada large": 1.00,
                            "angel evaporada small": 1.00,
                            "argentina corned beef large": 1.00,
                            "argentina corned beef regular": 1.00,
                            "argentina meat loaf large": 1.00,
                            "argentina meat loaf regular": 1.00,
                            "century tuna": 1.00,
                            "fresca sardines": 1.00,
                            "fresca tuna": 1.00,
                            "giniling": 1.00,
                            "hokkaido": 1.00,
                            "hunts": 1.00,
                            "ligo": 1.00,
                            "lucky 7": 1.00,
                            "maling small": 1.00,
                            "maling large": 1.00,
                            "mega": 1.00,
                            "pineapple chunks": 1.00, 
                            "pineapple tidbits": 1.00,
                            "purefoods chinese style luncheon meat large": 1.00,
                            "purefoods chinese style luncheon meat regular": 1.00,
                            "purefoods corned beef": 1.00, 
                            "reno large": 1.00, 
                            "reno small": 1.00,
                            "rose bowl": 1.00,
                            "saba": 1.00,
                            "san marino": 1.00,
                            "shanghai luncheon meat large": 1.00,
                            "wow ulam": 1.00,
                            "young's town": 1.00},  
        "Biscuits": {"bingo": 1.00,
                     "cal cheese": 1.00,
                     "cheese cake": 1.00,
                     "choochoo": 1.00,
                     "combi": 1.00, 
                     "cream-o": 1.00,
                     "crossini": 1.00,
                     "doowee donut": 1.00,
                     "ec": 1.00,
                     "fita": 1.00,
                     "fudgee bar": 1.00,
                     "hansel crackers": 1.00,
                     "hansel mocha/chocolate": 1.00,
                     "hello": 1.00,
                     "lion": 1.00,
                     "long marshmallow": 1.00,
                     "monde": 1.00,
                     "nissin": 1.00,
                     "oreo": 1.00,
                     "presto": 1.00,
                     "rebisco crackers": 1.00, 
                     "skyflakes crackers": 1.00, 
                     "skyflakes strawberry/chocolate": 1.00,
                     "tiger": 1.00,
                     "wafrets": 1.00}, 
        "Beverages": {}, 
        "Shampoo & Conditioners": {}, 
        "Laundry Products": {}
    }

    for category in categories:
        print(category)

    category = input("\nChoose a category: ").title()
    print()

    print_category(category, categories)
        
    item = input("\nItem: ")
    print(f"Price for {item} is: {categories[category][item]}")

main()