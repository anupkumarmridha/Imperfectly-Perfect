from django.urls import path
from account import views
import home
# app_name = 'home'
urlpatterns = [


  path('/signup/', views.handelSingup, name='handelSingup'),
  path('/register', views.register, name='register'),
  
  path('/login', views.handleLogin, name='handleLogin'),
  path('/logout', views.handleLogout, name='handleLogout'),

  path('/admin', views.company_home, name='admin_home'),
  path('/customer-home', views.customer_home, name='customer_home'),
  path('/company-home', views.company_home, name='company_home'),

  #CRUD Customer profile
  path("add-customer", views.add_customer, name='add_customer'),
  path("add-profile-details/<int:id>", views.add_customer_profile_details, name='add_customer_profile_details'),
  path("view-all-customer-profile/", views.view_all_customer_profile, name='view_all_customer_profile'),
  path("view-customer-profile/<int:id>", views.view_customer_profile, name='view_customer_profile'),
  path("update-customer-profile/<int:id>", views.update_customer_profile, name='update_customer_profile'),
  path("update-customer-password/<int:id>", views.update_customer_password, name='update_customer_password'),
  path("delete-customer-profile/<int:id>", views.delete_customer_profile, name='delete_customer_profile'),

  #CRUD Company profile
  path("add-company", views.add_company, name='add_company'),
  path("add-profile-details/<int:id>", views.add_company_profile_details, name='add_company_profile_details'),
  path("view-all-company-profile/", views.view_all_company_profile, name='view_all_company_profile'),
  path("company-details/<int:pk>", views.company_details, name='company_details'),
  path("update-company-profile/<int:id>", views.update_company_profile, name='update_company_profile'),
  path("update-company-password/<int:id>", views.update_company_password, name='update_company_password'),
  path("delete-company-profile/<int:id>", views.delete_company_profile, name='delete_company_profile'),

  # My winigs product
  path("my-winings", views.win_products_list, name='my_win_products'),
  path("my-bids", views.bid_products_list, name='bid_products_list'),
]