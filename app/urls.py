from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('expert_user/', expert_user, name='expert_user'),
    path('normal_user/', normal_user, name='normal_user'),

]
