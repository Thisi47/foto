import authentification.views as au_vs
import blog.views as bg_vs
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name = "authentification/login.html", 
        redirect_authenticated_user=True
    ), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('home/', bg_vs.home, name="home"),
    path('signup/', au_vs.signup_page, name="signup"),
]
