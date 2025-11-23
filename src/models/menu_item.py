# menu item model: MongoEngine document for menu item details

from mongoengine import *
from src.utils.constants import MENU_CATEGORIES

class MenuItem(Document):
    # menu item details
    name = StringField(required=True, max_length=100)
    category = StringField(required=True, choices=MENU_CATEGORIES)
    price = FloatField(required=True, min_value=0)
    cost = FloatField(required=True, min_value=0)
