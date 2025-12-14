# event model: MongoEngine document for event details, financials, and computed fields

from mongoengine import *
from src.utils.constants import EVENT_TYPES

class Event(Document):
    # event info and financials
    client_name = StringField(required=True, max_length=100)
    event_date = DateField(required=True)
    event_type = StringField(required=True, choices=EVENT_TYPES)
    food_sales = FloatField(default=0, min_value=0)
    bev_sales = FloatField(default=0, min_value=0)
    total_sales = FloatField(default=0, min_value=0)
    food_cost = FloatField(default=0, min_value=0)
    bev_cost = FloatField(default=0, min_value=0)
    total_cost = FloatField(default=0, min_value=0)

    # auto compute totals before saving
    # referenced: https://docs.mongoengine.org/apireference.html#documents
    def save(self, *args, **kwargs):
        self.total_sales = round(self.food_sales + self.bev_sales, 2)
        self.total_cost = round(self.food_cost + self.bev_cost, 2)
        return super().save(*args, **kwargs)
    
    # compute event name for display without storing in DB
    @property
    def display_name(self):
        return f"{self.client_name} {self.event_type}"
    
    meta = {
        'ordering': ['-event_date'],
        'indexes': [
            'event_type',
            ('event_date', 'event_type'),
            '-total_sales',
            '-total_cost'
        ],
        'auto_create_index': False
    }
