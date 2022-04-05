from django.contrib import admin
from account.models import User, Customer, Company
# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Company)
