# data_inputs/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import LoftRentalsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'data_inputs/index.html')

def loft_rental_form_view(request):
    if request.method == 'POST':
        form = LoftRentalsForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Optionally, redirect to a success page or do something else
            # return redirect('success')
    else:
        form = LoftRentalsForm()
    
    return render(request, 'data_inputs/loft_rental_form.html', {'form': form})





def registration_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional processing
            return redirect('data_inputs:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'data_inputs/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('data_inputs:index')  # Replace with the URL name of your index page
    else:
        form = AuthenticationForm()
    return render(request, 'data_inputs/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'data_inputs/logout.html')






@login_required
def dashboard(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User registered successfully!')
            return redirect('data_inputs:dashboard')  # Use the correct URL name for the dashboard page
    else:
        form = CustomUserCreationForm()
    return render(request, 'data_inputs/dashboard.html', {'form': form})




@login_required
def my_secure_view(request):
    # This view can only be accessed by logged-in users
    # Your view logic here
    return render(request, 'my_app/my_secure_view.html')
