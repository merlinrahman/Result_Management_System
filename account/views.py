
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page, cache_control
from django.contrib.auth import authenticate, login, logout
from account.forms import  UserRegistrationForm,UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache




# ***********************************************************************AUTHENTICATION*********************************************************
# REGISTRATION

@login_required(login_url='login')
def register(request):
    context={}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student registered successfully! ")
            return redirect('register')
        context['register_form'] = form
    else:
        form = UserRegistrationForm()
        context['register_form'] = form
    return render(request, 'result/register.html', context)



# CENTRAL UNIVERSITY EXAMS OFFICER LOGIN

def login_view(request):
    context={}
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request, user)
                return redirect("admin1")
        else:
            context['login_form'] = form
    else:
        form=UserLoginForm()
        context['login_form'] = form
    return render(request, "result/login_register.html", context)






# com sci login

@login_required(login_url='login')
def comsci_login(request):
    context={}
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request, user)
                return redirect("comsci_home_search")
        else:
            context['login_form'] = form
    else:
        form=UserLoginForm()
        context['login_form'] = form
    return render(request, "result/comsci_login.html", context)



# BIT LOGIN

@login_required(login_url='login')
def bit_login(request):
    context={}
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request, user)
                return redirect("bit_home_search")
        else:
            context['login_form'] = form
    else:
        form=UserLoginForm()
        context['login_form'] = form
    return render(request, "result/bit_login.html", context)



# BIT LOGIN

@login_required(login_url='login')
def masscom_login(request):
    context={}
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request, user)
                return redirect("masscom_home_search")
        else:
            context['login_form'] = form
    else:
        form=UserLoginForm()
        context['login_form'] = form
    return render(request, "result/masscom_login.html", context)


# LOGOUT

def logout_view(request):
    logout(request)
    return redirect('login_register')



# STUDENT-HOME
@login_required(login_url='login')
def student_home(request):
    return render(request, 'result/student_home.html', {})







