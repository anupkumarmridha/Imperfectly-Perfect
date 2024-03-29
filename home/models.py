from email.headerregistry import Address
from django.db import models
from account.models import User, Customer,Company
from ckeditor.fields import RichTextField
from django.db.models import Avg
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    title=models.CharField(max_length=255)
    
    author=models.ForeignKey(Customer, on_delete=models.CASCADE)
    order=models.BooleanField(default=False)
    product_image = models.ImageField(null=True, blank=True, upload_to='images/products/')
    
    desc=RichTextField(blank=True, null=True)
    
    price=models.DecimalField(max_digits=8, decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' | ' + str( self.author)

    @property
    def image_url(self):
        if self.product_image and hasattr(self.product_image, 'url'):
            return self.product_image.url


# class Watchlist(models.Model):
#     author = models.ForeignKey(Company, on_delete=models.CASCADE)
#     auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    

class Bid(models.Model):
    product = models.ForeignKey(Product, related_name="bids", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bid_price=models.DecimalField(max_digits=8, decimal_places=2)
    accepted_bid=models.BooleanField(default=False)         
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product) + ' | ' + str( self.company)
# class Bid(models.Model):
#     product = models.ForeignKey(Product, related_name="bids", on_delete=models.CASCADE)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)  
#     # time_starting = models.DateTimeField()
#     # time_ending = models.DateTimeField()      
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)

# class AcceptBid(models.Model):
#     bid=models.ForeignKey(Bid, related_name="accepted_bid", on_delete=models.CASCADE)
#     def __str__(self):
#         return str(self.bid)
    
class Order(models.Model):
    bid=models.ForeignKey(Bid, related_name="order" ,on_delete=models.CASCADE)
    delivery_date=models.DateField()
    shipping_partner=models.CharField(max_length=255)
    product_location=models.CharField(max_length=255)
    delivery_address=models.CharField(max_length=255)
    payment_status=models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.bid)

class Rating(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rate=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author=models.ForeignKey(Customer, on_delete=models.CASCADE)
    body=models.TextField()
    parrent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)


