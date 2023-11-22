

class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get the current session key if it exists
        cart = self.session.get('sesion_key') 

        #if the user is new, no session key, create
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}   

        #Make sure cart is available on all pages of the site
        self.cart = cart

    def add(self, product):
        product_id =  str(product_id)

        #Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        
        self.session.modified = True

