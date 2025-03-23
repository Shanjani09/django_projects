from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
@login_required(login_url='/accounts/login/')
def home_view(request):
    return render(request, "accounts/home.html") 
def custom_logout(request): 
    if request.method == 'POST': 
        logout(request) 
        return redirect('home')   
    else: 
        return HttpResponse(status=405) 
