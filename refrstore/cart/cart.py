from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    def __init__(self, request):
        """Inicjalizacja koszyka na zakupy"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #zapis pustego koszyka na zakupy w sesyji
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """Dodanie produktu do kosza lub zmiana jego ilości."""
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id][]'quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """oznaczenie sesji jako zmodyfikowane, aby na pewno była zapisana"""
        self.session.modified = True

    def remove(self, product):
        """Usuwanie produktu z koszyka na zakupy"""
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """iteracja przez elementy koszyka na zakupy i pobranie produktu z bazy danych"""
        products = Product.object.filter(id__in=product_id)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yeld item

    def __len__(self):
        """Obliczanie liczby wszystkich elementów w koszyku"""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Obliczanie sumy całkowitej ceny produktów w koszyku"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """Usuwanie koszyka na zakupy w sesji"""
        del self.session[sessings.CART.SESSION.ID]
        self.save()
