from django.urls import path
from champagne.views import *

app_name = 'champagne'

urlpatterns = [
    path('champagne/create', ChampagneCreateView.as_view()),
    path('all/', ChampagneListView.as_view()),
]