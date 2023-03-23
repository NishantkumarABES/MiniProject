from django.contrib import admin
from django.urls import path,include
from login import views
urlpatterns = [
    path("",views.login,name="login"),
    path("landingPage/",views.landingPage,name="landingPage"),
    path("instructionPage/",views.instruction,name="instruction"),
]
#path("",views.index,name='Login'),