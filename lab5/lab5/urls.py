"""
URL configuration for lab5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from trainee.views import *
from django.contrib.admin import *
from accounts.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("Account/", include("account.urls")),
    path("Track/", include("track.urls")),
    path("Trainee/", include("trainee.urls")),
    # path("Trainee/", TraineeListG, name="trainee-list"),
    path("accounts/login/", views.LoginView.as_view(), name="login"),
    # path("Register", register, name="register"),
    # path("", login, name="login"),
    # path("Register", include("accounts.urls")),
    # path("Register", views.R.as_view(), name="register"),
    # path("accounts/profile/", views.FormView.as_view(), name="profile"),
    # path("Logout/", views.LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
