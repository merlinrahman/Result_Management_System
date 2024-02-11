from django.shortcuts import render

# Create your views here.

# **************INDEX PAGE***********************.
def index(request):
    return render(request, 'result/index.html',{})

# **************ABOUT PAGE***********************.
def about(request):
    return render(request, 'result/about.html',{})

# **************CONTACT PAGE***********************.
def contact(request):
    return render(request, 'result/contact.html',{})

# **************CONTACT PAGE***********************.
def login_register(request):
    return render(request, 'result/login_register.html',{})