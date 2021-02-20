from django.urls import path
from champagne.views import *

app_name = 'champagne'

urlpatterns = [
    path('all/', ChampagneListView.as_view()),
    path('champagne/create', ChampagneCreateView.as_view()),
    path('champagne/detail/<int:pk>', ChampagneDetailView.as_view()),
]