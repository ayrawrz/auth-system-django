from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    form = UserCreationForm()
    isvalid = False

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()

            isvalid = True

            return HttpResponseRedirect(reverse('home'))

    return render(request, 'signup.html',context={
        'form': form, 
        'isvalid': isvalid
        
        })

def signin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Note: changed from request.POST to data=request.POST
        if form.is_valid():  # You need to check if form is valid first
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
        
        # If authentication fails or form is invalid, return the form with errors
        return render(request, 'signin.html', context={'form': form})
    
    # GET request - return the empty form
    return render(request, 'signin.html', context={'form': form})

@login_required()
def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('auth:signin'))