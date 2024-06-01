from django.shortcuts import render
from forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def login_page(request):
    form = LoginForm()
    message  = ''

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                message = f"Bonjour, {user.username} ! Vous etes connecte !"
            else:
                message = "Identifiant invalide !"

    return render(request, 'authentification/login.html', {
        'form': form,
        'message': message
    })