"""evote URL Configuration

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
from evoteUser import views as evoteuser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',evoteuser.login,name='login'),
    path('logout/',evoteuser.logout,name='logout'),
    path('register/',evoteuser.register,name='register'),
    path('createVoteCase/',evoteuser.createVoteCase,name='createVoteCase'),
    path('login_intro/',evoteuser.loginIntro,name='login_intro'),
    path('add_votecase/',evoteuser.addVoteCase,name='add_votecase'),
    path('add_candidate/',evoteuser.addCandidate,name='add_candidate'),
    path('view_votecase/',evoteuser.viewVoteCase,name='viewVoteCase'),

]
