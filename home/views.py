from email.mime import message
from logging import exception
from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.urls import is_valid_path
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from account.models import Company, Customer
from home.models import Category, Product,Bid, Order
from home.forms import PostProductForm, EditProductForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from account import views

# category
context={}
cats_menu=Category.objects.all()
context['cats_menu']=cats_menu

# Create your views here.
def homeView(request):
    return render(request,'home/index.html', context)



def search(request):
    return render(request,'home/index.html')

# category

def add_category(request):
    return render(request,'home/index.html')

def category_details(request,cats):
    category=Category.objects.get(name=cats)
    all_cats_product=Product.objects.filter(category=category)
    context={
        'all_cats_product':all_cats_product,
    }
    return render(request,'product/category_details.html',context)

def all_category_details(request):
    cats_menu=Category.objects.all()
    context={'cats_menu':cats_menu}
    # for i in context:
    #     print(i)
    print(request.path_info)
    return HttpResponseRedirect(request.path_info, context)

def update_category(request,cats):
    return render(request,'home/index.html')

def delete_category(request,cats):
    return render(request,'home/index.html')





# Product
def add_product(request):
    if request.method=='POST':
        form=PostProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "your Product has successfully added")
            return redirect('all_product_details')
        else:
            messages.success(request, "Form is Not Valid")
    else:
        form=PostProductForm()
    context['form']= form
    return render(request,'product/add_product.html', context)


def product_info(request,pk):
    product=Product.objects.get(id=pk)
    context={'product':product}
    return render(request,'product/index.html', context)

# def product_details(request,pk):
#     product_id=request.POST.get('product_id')
#     product_details=Product.objects.all
#     return render(request,'product/product_details.html',product_id)

class ProductDetailsView(DetailView):
    model=Product
    template_name='product/product_details.html'

def all_product_details(request):
    all_products=Product.objects.all()
    # context['all_products']=all_products
    product_id=request.GET.get('product_id')
    # for i in all_products:
    #     i.order=False
    #     i.save()


    # all_bids=Bid.objects.all()
    
    print(product_id)
    context={
        'all_products':all_products,
        # 'all_bids':all_bids,
    }
    return render(request,'product/view_all_product.html', context)


def customer_product_list(request,pk):
    try:
        pk=Customer.objects.get(user=request.user)
        # print(pk)
        all_posted_product=Product.objects.filter(author=pk).order_by('created_at')
        context['all_posted_product']=all_posted_product
        
        # all_bids
        all_bids=Bid.objects.all()
    except:
        messages.warning(request, "You have no Product")
        return redirect('all_product_details')
    return render(request,'product/customer_product_list.html',context)


class delete_product(DeleteView):
    model=Product
    template_name='product/delete_product.html'
    
    def get_success_url(self):
        pk=Customer.objects.get(user=self.request.user)
        # print(pk)
        return reverse( 'customer_product_list', kwargs={'pk': pk.id})

class update_product(UpdateView):
    model=Product
    form_class=EditProductForm
    template_name='product/update_product.html'
    
    def get_success_url(self):
        pk=Customer.objects.get(user=self.request.user)
        # print(pk)
        return reverse( 'customer_product_list', kwargs={'pk': pk.id})




def rating_product(request,pk):
    return render(request,'home/index.html')

# Comments
def add_comment(request):
    return render(request,'home/index.html')

def comment_details(request,pk):
    return render(request,'home/index.html')

def all_comment_details(request):
    return render(request,'home/index.html')

def update_comment(request,pk):
    return render(request,'home/index.html')

def delete_comment(request,pk):
    return render(request,'home/index.html')
  
# Customer product related functionality
def bid_details(request):
    try:
        pk=Customer.objects.get(user=request.user)
        all_posted_product=Product.objects.filter(author=pk).order_by('created_at')
        context={
            'all_posted_product':all_posted_product,             
            }
        return render(request,'product/bid_details.html',context)
    except:
        messages.warning(request, "You have no Bid details")
        return redirect('all_product_details')

def add_bid(request):
    if request.method=='POST':
        product_id = request.POST.get('product_id')
        company_id = request.POST.get('com_user_id')
        bid_price = request.POST['bid_price']
        try:

            product=Product.objects.get(pk=product_id)
            company=Company.objects.get(pk=company_id)
            bid_status=None

            try:
                try:
                    bid = Bid.objects.get(product=product, company=company)
                    bid_status=bid
                
                except Exception as e:
                    messages.error(request,e)
                if bid_status==None:
                    try:
                        bid_model = Bid(product=product, company=company, bid_price=bid_price)
                        bid_model.save()
                        messages.success(request, "Your Bid has successfully added")
                        return redirect('all_product_details')
                    except Exception as e:
                        messages.error(request,e)
                        return redirect('all_product_details')
                else:
                    
                    bid_exist = Bid.objects.filter(id=bid_status.id).exists()
                    if bid_exist:
                        try:
                            print(bid_status.id)
                            bid = Bid.objects.get(id=bid_status.id)
                            print(bid.id)
                            bid.bid_price=bid_price
                            bid.save()
                            messages.success(request, "Your Bid has updated")
                            return redirect('all_product_details')
                        except Exception as e:
                            messages.error(request,e)
                            return redirect('all_product_details')
    
            except Exception as e:
                messages.error(request,e)
                return redirect('all_product_details')

        except Exception as e:
            print(e)
            messages.error(request, e)
            # messages.error(request, "Failed to Bid the Product!")
            return redirect('all_product_details')
    else:
        messages.error(request, "Invalid Method!")
        return redirect('all_product_details')

# def accept_bid(request,pk):
    
#     bid=Bid.objects.get(id=pk)
    
#     print(bid.product)
#     print(bid.product.author)
#     print(bid.company)
#     try:
#         accepted_bid=AcceptBid()
#         accepted_bid.bid=bid
#         # set product order=true
#         product=Product.objects.get(id=bid.product.id)
#         product.order=True
#         accepted_bid.save()
#         product.save()
#     except exception as e:
#         print(e)
#     return redirect('bid_details')

def accept_bid(request,pk):
    
    bid=Bid.objects.get(id=pk)
    
    print(bid.product)
    print(bid.product.author)
    print(bid.company)
    try:
        bid.accepted_bid=True
        # set product order=true
        product=Product.objects.get(id=bid.product.id)
        product.order=True
        bid.save()
        product.save()
    except exception as e:
        print(e)
    return redirect('bid_details')

def company_rating(request, pk):
    pass

def add_order_details(request,pk):
    bid=Bid.objects.get(id=pk)
    # print(bid.id)
    # print(bid.product.author.address)
    if request.method=='POST':
        print(bid.product.author.address)
        delivery_date=request.POST['delivery_date']
        shipping_partner=request.POST['shipping_partner']
        product_location=request.POST['product_location']
        delivery_address=request.POST.get('delivery_address')
        payment_status=request.POST['payment_status']
        try:
            order=Order(bid=bid,delivery_date=delivery_date,shipping_partner=shipping_partner,product_location=product_location,delivery_address=delivery_address, payment_status=payment_status)
            order.save()
            messages.success(request, "Order successfuly order")
            return redirect('view_order_details')
        except Exception as e:
            messages.error(request,e)
            return redirect('view_order_details')
  
    context={
        'bid':bid,
    }
    
    return render(request,'orders/add_order_details.html',context)
def update_order_details(request,pk):
    bid=Bid.objects.get(id=pk)
    # print(bid.id)
    # print(bid.product.author.address)
    if request.method=='POST':
        delivery_date=request.POST.get('delivery_date')
        shipping_partner=request.POST.get('shipping_partner')
        product_location=request.POST.get('product_location')
        delivery_address=request.POST.get('delivery_address')
        payment_status=request.POST.get('payment_status')
        try:
            order=Order.objects.filter(bid=bid)
            order.delivery_date=delivery_date
            order.delivery_address=delivery_address
            order.shipping_partner=shipping_partner
            order.product_location=product_location
            order.payment_status=payment_status
            order.save()
            messages.success(request, "Order successfuly order")
            return redirect('view_order_details')
        except Exception as e:
            messages.error(request,e)
            return redirect('view_order_details')


    return render(request,'orders/add_order_details.html')
def view_order_details(request):
    # bid=Bid.objects.get(bid=pk)
    # order=Order.objects.get(id=id)
    # print(bid.bid_price)
    return render(request,'orders/view_order_details.html')