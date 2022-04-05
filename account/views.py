from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse
from account.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from account.models import User
from django.contrib import messages

from home import views 
# Create your views here.

def admin_home(request):
    return render(request, 'users/admin/admin_home.html')

def customer_home(request):
    return render(request,'users/customer/customer_home.html')
    
def company_home(request):
    return render(request,'users/company/company_home.html')

#.............................................registration..............................................#

def register(request):
    return render(request,'register/register.html')


def handelSingup(request):
    if request.method =='POST':

        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user_type=request.POST.get('user_type')
        #check for errorneous input
        print(user_type)

        if pass1 != pass2 :
            messages.error(request, "Password do not match.")
            return redirect('handelSingup')    

        #Create User
        try:
            myuser = User.objects.create_user(username=username, password=pass1, email=email, first_name=fname, last_name=lname, user_type=user_type)

            myuser.save()
            messages.success(request, "Account Created Successfully!")
            return redirect(views.homeView)

        except:
            messages.error(request, "Failed to SignUp!")
            return redirect('home')
    else:
        return HttpResponse("404 - Not Found")


def handleLogin(request):
    if request.method !='POST':
        return HttpResponse('Submission outside this window is not allowed 😎')
    else:
        #Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user =EmailBackEnd.authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfuly logged in 🥰")
            user_type = user.user_type
            print(user_type)
            #print("username : "+ request.POST.get("loginusername")+ "Password: " +request.POST.get("loginpassword"))
                
            if user_type == "1":
                # return HttpResponse("Student Login")
                return redirect('admin_home')

            elif user_type == '2':
                # return HttpResponse("Student Login")
                return redirect('customer_home')

            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('company_home')
        else:
            messages.error(request, "Invalid credentialsl, Please try again 😎")
            return redirect(views.homeView)

def handleLogout(request):
    if request.method=='POST':
        value=request.POST['value']
        logout(request)
        messages.success(request, "Successfuly logged out 🥰")
        
        return redirect(views.homeView)
    else:
        return HttpResponse('Sorry No Users Logged in 😎') 

#...............................profile details customer..........................#
def add_customer_profile_details(request,id):
    pass

def view_all_customer_profile(request):
    pass

def view_customer_profile(request,id):
    pass

def update_customer_password(request,id):
    pass

def update_customer_profile(request,id):
    pass

def delete_customer_profile(request,id):
    pass


# .....................profile details company.........................# 
def add_company_profile_details(request):
    pass

def view_all_company_profile(request):
    pass

def view_company_profile(request,id):
    pass


def update_company_password(request,id):
    pass

def update_company_profile(request,id):
    pass

def delete_company_profile(request,id):
    pass

# ........................my win product list for company.................#

def my_win_products(request):
    return render(request, 'users/company/my_win_product.html')