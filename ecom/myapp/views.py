from django.shortcuts import render
from .forms import Registration,LoginForm
from .models import UserRegistration,UserLogin

def home(request):
    return render(request,'home.html')
def product(request):
    return render(request,'product.html')
def errormessage(request):
    return render(request,'errormessage.html')
def register(request):
    if request.method == "POST":
        form =Registration(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html')

    else:
        form= Registration()
    return render (request,'register.html')

def login(request):
    if request.method== 'POST':
        form = LoginForm(request.POST)
        if form .is_valid():
            username=form['username'].valid()
            password=form['password'].valid()
            try:
                user=Login.object.get(username=username,password=password)
                if user is not None:
                    return render(request,'product.html')
            except:
                pass

    else:
        return render(request,'login.html')