from django.urls import path
from home import views

urlpatterns = [

    path('', views.homeView, name='homeView'),

    path('search', views.search, name='search'),

# ends point for category
    path('add-category', views.add_category, name='add_category'),
    path('category-details/<str:cats>', views.category_details, name='category_details'),
    path('all-category-details', views.all_category_details, name='all_category_details'),
    path('update-category/<str:cats>', views.update_category, name='update_category'),
    path('delete-category/<str:cats>', views.delete_category, name='delete_category'),

# ends point for products
    path('add-product', views.add_product, name='add_product'),
    path('product-info/<int:pk>', views.product_info, name='product_info'),
    path('product-details/<int:pk>', views.ProductDetailsView.as_view(), name='product_details'),
    path('all-product-details', views.all_product_details, name='all_product_details'),
    
    
    path('rating-product/<int:pk>', views.rating_product, name='rating_product'),
    
    path('company_rating/<int:pk>', views.company_rating, name='company_rating'),

#end's point for a user to perform product related operation
    path('bid-details', views.bid_details, name='bid_details'),
    path('customer-product-list/<int:pk>', views.customer_product_list, name='customer_product_list'),
    path('update-product/<int:pk>', views.update_product.as_view(), name='update_product'),
    path('Product/Delete/<int:pk>', views.delete_product.as_view(), name='delete_product'),

#end point for bids
    path('add-bid', views.add_bid, name='add_bid'),
    path('accept-bid/<int:pk>', views.accept_bid, name='accept_bid'),
#end point for comments

    path('add-comment', views.add_comment, name='add_comment'),
    path('comment-details/<int:pk>', views.comment_details, name='comment_details'),
    path('all-comment-details', views.all_comment_details, name='all_comment_details'),
    path('update-comment/<int:pk>', views.update_comment, name='update_comment'),
    path('delete-comment/<int:pk>', views.delete_comment, name='delete_comment'),
# end point for orders
    path('add_order_details', views.add_order_details, name='add_order_details'),
    path('view_order_details', views.view_order_details, name='view_order_details'),
]