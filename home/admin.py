from django.contrib import admin
from home.models import Category, Product, AcceptBid, Bid, Rating, Review, Auction
# Register your models here.
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(AcceptBid)
admin.site.register(Bid)
admin.site.register(Rating)
admin.site.register(Review)