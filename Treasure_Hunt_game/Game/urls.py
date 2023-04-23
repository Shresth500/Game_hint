from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
    path('account/',views.account,name="account"),
    path('start_game/',views.start_game,name="start_game"),
    path('details/',views.details,name="details"),
    path('stats/',views.stats,name="stats"),
    path('ends/',views.ends,name="end"),
]