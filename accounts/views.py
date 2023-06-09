from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User

from contacts.models import Contact

# Create your views here.
def login(request):
    if request.method == "POST":
        # Login user
        username = request.POST['username']
        password = request.POST['password']
        # Create user entity
        user = auth.authenticate(username=username,
                                 password=password)
        # Check, if user exists
        if user is not None:
            # login and redirect to the dashboard
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            # Invalid credentials for user
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is been used')
                    return redirect('register')
                else:
                    # Looks good
                    ...
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
                    # Login after registration
                    # auth.login(request, user)
                    # messages.success(request, 'You are logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            # Alert 
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    contact_list = Contact.objects.all().order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': contact_list
    }
    return render(request, 'accounts/dashboard.html', context=context)