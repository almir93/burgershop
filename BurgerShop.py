##########################
# Classes and Variables #
########################

class FoodItem:
    name = ''
    price = ''

    def __init__(self, name, price):
        self.name = name
        self.price = price
    def set_name(self, name):
        self.name = name
    def set_price(self, price):
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price

class Burger(FoodItem):
    bun = ''
    patty = ''
    cheese = ''
    toppings = []
    description = ''

    def __init__(self, name, price, bun, patty, cheese, topp, desc):
        super().__init__(name, price)
        self.bun = bun
        self.patty = patty
        self.cheese = cheese
        for item in topp:
            self.toppings.append(item)
        self.description = desc

class Drink(FoodItem):
    size = ''

    def __init__(self, size, name, price):
        super().__init__(name, price)
        self.size = size


class Side(FoodItem):
    size = ''

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size


class Combo(FoodItem):
    entree = None
    side = None
    drink = None

    def __init__(self, name, price, ent, side, drink):
        super().__init__(name, price)
        self.entree = ent
        self.side = side
        self.drink = drink


class Order:
    num = None
    items = []
    total = 0

    def __init__(self, item):
        self.items.append(item)
    def add_item(self, item):
        self.items.append(item)
    def calc_total(self):
        for it in self.items:
            self.total += it.get_price()
        return self.total


#####################
# Helper Functions #
###################

def user_input_burger():
    # ask user for input and store it in burger object
    counter = 1
    for i in menu[1].keys():
        print (i.get_name(), i.description, "(", counter, ")")
    selected_burger = input("What is your choice? ")    
    if selected_burger == 0:     
        name = "Build your own"
        price = 12.99
        bun = input("What type of bun would you like? ")
        patty = input("What type of patty would you like? ")
        topp = input("What temp would you like it to be cooked? ")
        b = Burger(name, price, bun, patty, temp)

    return b


def user_input_drink():
    # ask user for input and store it in drink object
    for drink in drink_dict:
        print(drink)
    drink_order = input("Which drink would you like? ")
    d = Drink(drink_order, drink_dict[drink_order])

    return d


def user_input_side():
    s = Side()
    # ask user for input and store it in side object
    return s


def user_input_combo():
    c = Combo()
    # ask user for input and store it in combo object
    # a combo must include one burger, one side, and one drink
    return c


def take_order():
    # ask user for name for the order
    # repeat taking order until client is done
    # display order details
    # display a thank you message
    print("Welcome to Burger Shop\n\n")
    more = True
    count = 0
    while more != False:
        if count == 0:
            print("What can I get you started with? ")
        else:
            print("Select an item or enter 0 to quit\n")
            selected_item = input("A Burger(1), Drink(2), Side(3), or make a Combo(4) ")
            if selected_item == 0:
                more = False
            else:
                if selected_item == 1:
                    user_input_burger()
                elif selected_item == 2:
                    user_input_drink
                elif selected_item == 3:
                    user_input_side()
                elif selected_item == 4:
                    user_input_combo()
                else:
                    print("Please enter a valid option")
            count = count + 1
    print("\n Thanks for placing your order with us! ")


###############
# Menu Items #
#############

menu = {
    "Burgers" : {
        "The AJ" : Burger("The AJ", 14.00, "Ciabatta", "Veggie Patty", "Gouda", ["avocado", "onion", "arugula", "mushrooms"], \
            "Beautifully crafted sandwich on a ciabatta roll with a veggie patty, gouda, avocado, onion, arugula, and mushroom"),
      
        "The Big Al" : Burger("The Big Al", 17.00, "plain", "Sirloin", "American Cheese", ["lettuce", "tomato", "mayo", "pickles"], \
            "Our most popular burger option!! Filled with a thick soft juicy patty. Comes with lettuce,tomato,mayo,and pickles"),
      
        "The Triple Bypass" : Burger("The Triple Bypass", 22.00, "Brioche", "Angus Patty", "Cheddar", ["grilled onions", "bacon"], \
            "Six All-American Angus patties topped with cheddar, grilled onions and a mountain of bacon!!! So good that you won't \
                even regret saying goodbye to your family!")
    },

    "Sides" : {

    },

    "Drinks" : {

    }
}


take_order()
