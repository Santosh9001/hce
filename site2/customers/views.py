from django.shortcuts import redirect, render

from .forms import CustomerSignupForm
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
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
        