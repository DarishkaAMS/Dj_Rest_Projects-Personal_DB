from django.contrib import admin
from django.urls import path, include
from champagne.views import *

app_name = 'champagne'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('champagne/create', ChampagneCreateView.as_view()),
]