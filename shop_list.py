''' You need to ask the user for the input.

- A user should be able to create a shopping list. A shopping list consists
of a title and description. Example = Fiesta, Walmart, Sams Club, Cosco, Randalls etc 

- A user should be able to add multiple shoppings lists 

- Give user an option to display the list 

- A user should be able to add a grocery items to a particular shopping list.
A grocery item consists of a title. Example Milk, Cookies, Paper, Napkins,
Soda, Chips etc '''

class Grocery ():
    def __init__(self,title):
        self.title = title
        

class Shopping_list ():
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.store_list = []

    def list_summary (self):
        print("{0}: store:{1}".format(self.title, self.description))
    
    def viewall_items (self):
        for item in self.store_list:
            print(item.title)

while True:
    shop_name = input("Enter shopping list name: 'or press Q to quit at any time' ").title()
    if(shop_name == "q"):
        break

    store_name = input("Enter store name: ").title()
    if(store_name == "q"):
        break
    shop_list = Shopping_list(shop_name,store_name)

    while True:
        store_items = input("Enter items here: ").lower()
        if(store_items == "q"):
            Display_list = input("Do you view your shopping list, y or n? ").lower()
            if (Display_list == "y"):
                shop_list.list_summary()
                shop_list.viewall_items()
            else:
                break
            break
        else:
            item1 = Grocery(store_items)
            shop_list.store_list.append(item1)
            print(len(shop_list.store_list))

    
