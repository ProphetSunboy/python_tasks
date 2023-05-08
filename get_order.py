def get_order(order):
    '''
    Input example: "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
    Function returns string with spaces and capitals like so:
    "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke".
    Items will be in the same order as they appear in the menu. 
    '''
    menu = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    return ' '.join(' '.join([meal.capitalize()] * order.count(meal)) for meal in menu if order.count(meal) > 0)