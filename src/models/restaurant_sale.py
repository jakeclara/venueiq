# restaurant sale model: MongoEngine document for itemized restaurant sales

from mongoengine import *
from src.models.menu_item import MenuItem
from datetime import date

class RestaurantSale(Document):
    # sale details
    sales_date = DateField(required=True, default=date.today)
    item = ReferenceField(MenuItem, required=True)
    category = StringField(required=True)
    quantity = IntField(required=True, min_value=1)
    total_sales = FloatField(default=0, min_value=0)
    total_cost = FloatField(default=0, min_value=0)

    # auto compute totals before saving
    def save(self, *args, **kwargs):
        self.total_sales = round(self.item.price * self.quantity, 2)
        self.total_cost = round(self.item.cost * self.quantity, 2)
        return super().save(*args, **kwargs)
    
    meta = {
    'ordering': ['-sales_date'],
    'indexes': [
        'sales_date',
        'item',
        '-total_sales',
        '-total_cost',
        ('sales_date', 'category'), 
        ('sales_date', 'item'),
    ],
    'auto_create_index': False
    }
    