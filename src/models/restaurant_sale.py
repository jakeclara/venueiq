# restaurant sale model: MongoEngine document for itemized restaurant sales

from mongoengine import *
from src.models.menu_item import MenuItem
from datetime import date

class RestaurantSale(Document):
    # sale details
    date = DateField(required=True, default=date.today)
    item = ReferenceField(MenuItem, required=True)
    quantity = IntField(required=True, min_value=1)
    total_sales = FloatField(default=0, min_value=0)
    total_cost = FloatField(default=0, min_value=0)

    # auto compute totals before saving
    def save(self, *args, **kwargs):
        self.total_sales = self.item.price * self.quantity
        self.total_cost = self.item.cost * self.quantity
        return super().save(*args, **kwargs)
    
    meta = {
    'ordering': ['-date'],
    'indexes': ['date', 'item', '-total_sales', '-total_cost']
    }