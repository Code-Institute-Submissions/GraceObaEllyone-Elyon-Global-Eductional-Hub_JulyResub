

def cart_contents(request):

    cart_items = []
    total = 0

    cart = request.session.get('cart', {})

    last_item = request.session.get('last_item', {})

