"""simple_votings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import include, path

from polls import views

from polls.forms import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),  # Index page
    path('register/', views.register, name='register'),  # Sign up
    path('login/', CustomLoginView.as_view(template_name='pages/login.html', extra_context={'pagename': "Login"}), name='login'),  # Sign in
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),  # Log out
    path('add_poll/', views.add_poll, name='add_poll'),  # Add a new poll
    path('view_polls/', views.view_polls, name='view_polls'),  # See all polls
    path('view_poll/<poll_id>', views.view_poll, name='view_poll'),  # See a poll
    path('vote/<poll_id>/', views.vote, name='vote'),  # Vote for a poll
]
