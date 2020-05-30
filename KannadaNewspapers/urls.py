"""KannadaNewspapers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newspapers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_user/', views.login_user,name="login_user"),
    path('forgot_password/', views.forgot_password,name="forgot_password"),
    path('state/', views.state,name="state"),
    path('district/', views.district,name="district"),
    path('company/', views.company,name="company"),
    path('headline/', views.headline,name="headline"),
    path('magzine_catagory/', views.magzine_catagory,name="magzine_catagory"),
    path('magzine/', views.magzine,name="magzine"),
    path('sunday_magzine/', views.sunday_magzine,name="sunday_magzine"),
    path('publish_newspaper/', views.publish_newspaper,name="publish_newspaper"),
]
