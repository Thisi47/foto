import authentification.views as vs
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vs.login_page, name="login"),
]
