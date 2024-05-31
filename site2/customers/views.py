from django.shortcuts import redirect, render

from .forms import CustomerSignupForm
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.

# def signup(request):
#     customer = None
#     if request.method == 'POST':
#         form = CustomerSignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             customer = Customer.objects.all()
#             return render(request,'customers/customer_details.html',{'customer': customer})
#     else:
#         form = CustomerSignupForm()
        
#     form = CustomerSignupForm()
#     customer = Customer.objects.all()
#     return render(request,'customers/signup.html',{'form':form,'customer':customer})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(request)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
        
def set_session(request):
    # Set a session key-value pair
    request.session['name'] = 'Himalayan College'
    return HttpResponse("Session data set")

def get_session(request):
    # Retrieve a session value
    name = request.session.get('name', 'Guest')
    return HttpResponse(f"Hello, {name}")

def del_session(request):
    # Delete a session value
    try:
        del request.session['name']
    except KeyError:
        pass
    return HttpResponse("Session data deleted")

def set_cookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('name', 'New Cookie', max_age=3600)  # Cookie expires in 1 hour
    return response

def get_cookie(request):
    name = request.COOKIES.get('name', 'Guest')
    return HttpResponse(f"Hello, {name}")

def del_cookie(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('name')
    return response