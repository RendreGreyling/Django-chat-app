from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def homepage(request):
    return render(request, 'coreapp/homepage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('homepage')
    else:
        form = SignUpForm()
    
    return render(request, 'coreapp/signup.html', {'form': form})

