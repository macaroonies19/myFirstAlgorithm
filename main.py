Order = 'none'
OrderMore = 'none'
print(Order)
def menu():
    Menu = ['Burger, Chocolate Milk, Garlic Bread, Juice, Pasta, Scroll']
    Prices = [5.00, 2.50, 2.00, 2.50, 6.50]
    print("Menu:")
    print(Menu)
    print(Prices)
    Order = input('What would you like? ')
    return menu()

def order():
    print('Added to cart')
    OrderMore = input('Would you like anything else? ')
    if OrderMore == 'yes':
        Order2 = input('What else would you like? ')
    else:
     return order()

order()
menu()