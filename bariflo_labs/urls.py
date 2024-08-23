from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup_get/',views.signup_get),
    path('signup_post/',views.signup_post),
    path('login/',views.login),
    
]
