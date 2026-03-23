_cart = []

def clear():
    _cart.clear()

def cart():
    return _cart

def add(item):
    _cart.append(item) 

    def print_cart():
        for item in _cart:
            print(item)