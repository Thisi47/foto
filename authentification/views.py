from django.shortcuts import render, redirect
from authentification.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.views.generic import View

class Login_page(View):
    form_class = LoginForm
    template_name = 'authentification/login.html'
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, {
        'form': form,
        'message': message
        })

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            message = 'Identifiants invalides.'
        return render(request, self.template_name, {
        'form': form,
        'message': message
        })



def logout_user(request):
    logout(request)
    return redirect('login')

def signup_page(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)


    return render(request, 'authentification/signup.html', { 'form': form })
        