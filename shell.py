from shop.models import Item, Purchase

item_1 = Item.objects.create(name='Korea', price=10000)
item_2 = Item.objects.create(name='New York', price=20000)


item_1.purchase.create(name='Daulet', age=16)
item_2.purchase.create(name='Buster', age=24)

item_1.save()
item_2.save()