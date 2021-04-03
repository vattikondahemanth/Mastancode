############################  11.20  Start #############################
'''

class FoodItem:
    # TODO: Define constructor with parameters to initialize instance 
    #       attributes (name, fat, carbs, protein)
    def __init__(self, name=None, fat = 0.0, carbs = 0.0, protein = 0.0) -> None:
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        

    def get_calories(self, num_servings=0.0):
        # Calorie formula  
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings  
        return calories
       
    def print_info(self):
        result =( ('Nutritional information per serving of {}:'.format(self.name)) + '\n'
        + ('Fat: {:.2f} g'.format(self.fat)) + '\n'
        + ('Carbohydrates: {:.2f} g'.format(self.carbs)) + '\n'
        + ('Protein: {:.2f} g'.format(self.protein)) + '\n' )
        print(result)

if __name__ == "__main__":
    
    food_item1 = FoodItem()
   
    item_name = input('Food Item Name: \n')
    amount_fat = float(input('Food Item Fat: \n'))
    amount_carbs = float(input('Food Item Carbohydrates: \n'))
    amount_protein = float(input('Food Item Protein: \n'))
   
    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
      
    num_servings = float(input('Food Item Servings: \n'))
    print(3 * '\n')
    food_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, 
                          food_item1.get_calories(num_servings)))
                           
    print()
                           
    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, 
                          food_item2.get_calories(num_servings)))

'''  

############################  11.20  End #############################


############################  11.21  Start #############################
'''
class Artist:
    def __init__(self, name= None, birth_year=0, death_year=0) -> None:
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
    
    def print_info(self):
        if self.death_year == -1:
            print('{}, born {}'.format(self.name, self.birth_year))
        else:
            print('{} ({}-{})'.format(self.name, self.birth_year, self.death_year))

      
class Artwork:
    def __init__(self, title = None, year_created=0, artist= Artist()) -> None:
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        print('Title: {}, {}'.format(self.title, self.year_created))


if __name__ == "__main__":
    user_artist_name = input('Artist Name: \n')
    user_birth_year = int(input('Artist birth year: \n'))
    user_death_year = int(input('Artist death year: \n'))
    artwork_title = input('Artwork Title: \n')
    artwork_year_created = int(input('Artwork Year Created: \n'))

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(artwork_title, artwork_year_created, user_artist)
    print(3 * '\n')
    user_artist.print_info()
    new_artwork.print_info()
'''

############################  11.21  End #############################



############################  11.22  Start #############################

'''

class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print('Base: {:.2f}'.format(self.base))
        print('Height: {:.2f}'.format(self.height))
        print('Area: {:.2f}'.format(self.get_area()))

if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    user_base = float(input('Triangle1 Base: \n'))
    triangle1.set_base(user_base)

    user_height = float(input('Triangle1 Height: \n'))
    triangle1.set_height(user_height)

    user_base = float(input('Triangle2 Base: \n'))
    triangle2.set_base(user_base)

    user_height = float(input('Triangle2 Height: \n'))
    triangle2.set_height(user_height)

    larger_traingle = triangle1 if triangle1.get_area()> triangle2.get_area() else triangle2
    print(3 * '\n')
    print('Triangle with larger area:')
    larger_traingle.print_info()

'''


############################  11.22  End #############################



############################  11.23  Start #############################

'''
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        total = self.team_wins + self.team_losses
        if total > 0:
            return self.team_wins / total
        else:
            return total


if __name__ == "__main__":
    
    team = Team()
   
    team_name = input('Team Name: \n')
    team_wins = int(input('Team wins \n'))
    team_losses = int(input('Team losses \n'))
    
    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses
    print(3*'\n')
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name,'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')
'''

############################  11.23  End #############################

############################  11.24  Start #############################
'''

class ItemToPurchase():
    def __init__(self, item_name= None, item_price= 0, item_quantity= 0, item_description= None) -> None:
        self.item_name: str = str(item_name)
        self.item_price: float = float(item_price)
        self.item_quantity: int = int(item_quantity)
        self.item_description: str = str(item_description)

    def print_item_description(self):
        print(self.item_description)
    
    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name,  self.item_quantity, self.item_price,  self.item_quantity * self.item_price))

if __name__== '__main__':
    
    print('Item 1')
    item_name = input('Enter the Item Name: \n')
    item_price = float(input('Enter the Item Price \n'))
    item_quantity = int(input('Enter the Item Quantity \n'))
    print('\n')
    item1 = ItemToPurchase(item_name, item_price, item_quantity)
    

    print('Item 2')
    item_name = input('Enter the Item Name: \n')
    item_price = float(input('Enter the Item Price \n'))
    item_quantity = int(input('Enter the Item Quantity \n'))
    item2 = ItemToPurchase(item_name, item_price, item_quantity)
    
    print('\n')
    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()

    print('TOTAL: {}'.format(
        (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
        ))
'''

############################  11.24  End #############################


############################  11.25  End #############################
'''
import datetime


class ItemToPurchase():
    def __init__(self, item_name= None, item_price= 0, item_quantity= 0, item_description= None) -> None:
        self.item_name: str = str(item_name)
        self.item_price: float = float(item_price)
        self.item_quantity: int = int(item_quantity)
        self.item_description: str = str(item_description)

    def print_item_description(self):
        print(self.item_description)
    
    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name,  self.item_quantity, self.item_price,  self.item_quantity * self.item_price))


class ShoppingCart():
    def __init__(self, customer_name=None, current_date=datetime.datetime(2016, 1, 1), cart_items=[]) -> None:
        self.customer_name: str = str(customer_name)
        self.current_date: datetime.datetime = current_date
        self.cart_items: list = cart_items
    
    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        item =  next((x for x in self.cart_items if x.item_name==item_name), None)
        self.cart.remove(item)

    def modify_item(self, item: ItemToPurchase):
        if next((x for x in self.cart_items if x.item_name==item.item_name), None):
            self.remove_item(item.item_name)
            self.add_item(item)
        else:
            print('Item not found in cart. Nothing modified.')
    
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    
    def get_cost_of_cart(self):
        return sum([x.item_price for x in self.cart_items])
    
    def print_total(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
            return
        
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date.strftime("%B %d, %Y")))
        print('Number of Items: {}'.format(len(self.cart_items)))
        print('\n')
        total = 0.0
        for i in self.cart_items:
            total += i.item_quantity * i.item_price
            i.print_item_cost()
        
        print('\n')
        print('Total: ${}'.format(total))
    
    def print_descriptions(self):
        for i in self.cart_items:
            print(i.print_item_description())

if __name__== '__main__':
    
    print('Item 1')
    item_name = input('Enter the Item Name: \n')
    item_price = float(input('Enter the Item Price \n'))
    item_quantity = int(input('Enter the Item Quantity \n'))
    print('\n')
    item1 = ItemToPurchase(item_name, item_price, item_quantity)
    

    print('Item 2')
    item_name = input('Enter the Item Name: \n')
    item_price = float(input('Enter the Item Price \n'))
    item_quantity = int(input('Enter the Item Quantity \n'))
    item2 = ItemToPurchase(item_name, item_price, item_quantity)
    
    print('\n')
    shopping_cart = ShoppingCart(customer_name="Hemanth", current_date=datetime.datetime.now())
    shopping_cart.add_item(item1)
    shopping_cart.add_item(item2)
    shopping_cart.print_total()

'''

############################  11.25  End #############################


############################  11.26  Start #############################

'''
class pt3d:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, obj):
        return '<{},{},{}>'.format(self.x + obj.x, self.y +  obj.y, self.z +  obj.z)

    def __sub__(self, obj):
        return (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 + (self.z - obj.z) ** 2

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y and self.z == obj.z

    def __str__(self):
        return '<{},{},{}>'.format(self.x, self.y, self.z)

if __name__ == '__main__':

    p1 = pt3d(1,1,1)
    p2 = pt3d(2,3,4)
    print("Point1 : ", p1)
    print("Point2 : ", p2)
    print(2*'\n')
    print('Addition: ', p1 + p2)
    print('Euclidean distance: ', p1 - p2)
    print('Equal: ', p1 == p2)

'''
############################  11.26  End #############################

