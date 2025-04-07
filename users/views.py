from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from users.forms import RegisterForm, CustomRegistrationForm


# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        form = CustomRegistrationForm()
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # confirm_password = form.cleaned_data.get('password2')

            # if password == confirm_password:
            #     User.objects.create(username=username, password=password)
            # else:
            #     print("Password are not same")
            form.save()

    return render(request, 'registration/register.html',{'form':form})



def sign_in(request):
    if request.method == 'POST':
        username = print(request.POST.get('username'))
        password = print(request.POST.get('password'))

        print("Doc", username, password)

        user = authenticate(request, username = username, password = password)

        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')