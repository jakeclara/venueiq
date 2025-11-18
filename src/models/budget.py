# budget model: MongoEngine document for budgeted financials

from mongoengine import *

class Budget(Document):
    # period
    month = IntField(required=True, min_value=1, max_value=12)
    year = IntField(required=True, min_value=2020, max_value=2040)

    # revenues
    food_sales = FloatField(default=0, min_value=0)
    bev_sales = FloatField(default=0, min_value=0)
    event_sales = FloatField(default=0, min_value=0)
    total_sales = FloatField(default=0, min_value=0)
    
    # costs
    food_cost = FloatField(default=0, min_value=0)
    bev_cost = FloatField(default=0, min_value=0)
    event_cost = FloatField(default=0, min_value=0)
    total_cost = FloatField(default=0, min_value=0)
    
    # profit
    gross_profit = FloatField(default=0)

    # auto compute totals and gross profit before saving
    def save(self, *args, **kwargs):
        self.total_sales = self.food_sales + self.bev_sales + self.event_sales
        self.total_cost = self.food_cost + self.bev_cost + self.event_cost
        self.gross_profit = self.total_sales - self.total_cost
        return super().save(*args, **kwargs)

    meta = {
        'ordering': ['-year', '-month'],
        'indexes': ['year', 'month']
    }