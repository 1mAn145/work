from django.urls import path
from apps.accounts.views import register , login , logout_form
urlpatterns = [
    path('register/',register, name='register'),
    path('login/',login, name='login'),
    path('logout/', logout_form, name='logout'),

]