from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user/', views.user, name="user"),
    path('form_url/', views.form_view, name="form_name"),
    path('signup/', views.userform, name="signup"),
]
